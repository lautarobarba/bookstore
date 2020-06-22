from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from shoppingcart.models import Order, OrderLine, ProductList 
from django.views.generic import ListView, DetailView
from django.views import View
from django.forms import Form
from datetime import datetime

### Necesario para hacer los pdfs
from io import BytesIO
from django.http import FileResponse
from django.template.loader import get_template

#from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
#import itertools
from django.http import HttpResponse
from xhtml2pdf import pisa
###

##PARA PODER ENCONTRAR LA IMAGEN DEL LOGO
from django.conf import settings
import os
from reportlab.lib.utils import ImageReader


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    template_name = 'shoppingcart/order_create.html'
    fields = '__all__'

    def get(self, request, *args, **kwargs):
        self.client = request.user
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_empty'] = self.client.cart.is_empty()
        return context

    def post(self, request, *args, **kwargs):
        u_client = request.user
        u_cart = request.user.cart
        #lineas = ProductList.objects.filter(cart=u_cart)
        cart_lines = u_cart.productlist_set.all()

        #Creo una nueva compra
        new_order = Order()
        #Datos del cliente
        if u_client.profile.first_name and u_client.profile.last_name:
            new_order.c_name = u_client.profile.first_name + ' ' +  u_client.profile.last_name
        else:
            new_order.c_name = 'Sin nombre'
        new_order.c_email = u_client.email
        new_order.c_profile_pk = u_client.profile.pk
        new_order.save()

        #Guardo los libros del carrito en la compra
        for l in cart_lines:
            #Por cada linea del carrito creo una linea de la orden
            new_order_line = OrderLine()

            #A que orden pertenece
            new_order_line.order = new_order

            #Datos del libro
            new_order_line.b_title = l.book.title
            new_order_line.b_editorial = l.book.editorial.name
            new_order_line.b_price = l.book.get_price()
            new_order_line.b_pk = l.book.pk
            new_order_line.quantity = l.quantity

            new_order_line.save()
            #Elimino los libros del carrito
            l.delete()
        return redirect(new_order)

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.client = request.user
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
            return Order.objects.filter(c_profile_pk=self.client.profile.pk)

class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'shoppingcart/order_detail.html'

class ResumeView(LoginRequiredMixin, ListView):
    model = Order
    form_class = Form
    template_name = 'shoppingcart/resume_list.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        mensaje = None
        today = datetime.now()

        if request.GET.get('day'):
            self.day = request.GET.get('day')
            self.year = today.year
            self.month = today.month
            mensaje = f'Día {self.day} del {self.month} del {self.year}'
        else:
            self.day = None

        if request.GET.get('month'):
            self.month = request.GET.get('month')
            self.year = today.year
            if self.day:
                mensaje = f'Día {self.day} del {self.month} del {self.year}'
            else:
                mensaje = f'Mes {self.month} del {self.year}'
        elif not self.day:
                self.month = None

        if request.GET.get('year'):
            self.year = request.GET.get('year')
            if self.month and self.day:
                mensaje = f'Día {self.day} del {self.month} del {self.year}'
            elif self.month:
                mensaje = f'Mes {self.month} del {self.year}'
            else:
                mensaje = f'Año {self.year}'
        elif not self.month and not self.day:
            self.year = None

        if mensaje:
            self.mensaje = 'Búsqueda para el ' + mensaje
        else:
            self.mensaje = None
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mensaje'] = self.mensaje
        return context

    def get_queryset(self):
        queryset = Order.objects.all()
        if self.day or self.month or self.year:
            if self.year:
                queryset =  queryset.filter(date__year=int(self.year))
            if self.month:
                queryset =  queryset.filter(date__month=int(self.month))
            if self.day:
                queryset =  queryset.filter(date__day=int(self.day))
        else:
            #queryset = queryset.filter(date__year=datetime.now().year, date__month=datetime.now().month, date__day=datetime.now().day)
            queryset = queryset.filter(date__year=1000)
        return queryset

class PrintOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'shoppingcart/order_print_error.html'

    def get(self, request, *args, **kwargs):

        def headerFooter(canvas ,doc):
            img_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'LogoCompleto.jpg')
            #print(img_path)
            #print(type(img_path))
            img = ImageReader(img_path)


            headerImg = 'imagenHeader' #PATH DEL LOGO
            hoy = datetime.now()
            headerDate = f'Fecha: {hoy.day}/{hoy.month}/{hoy.year}'
            footer = 'The Eye Of Minds - 2020'

            canvas.saveState()
            #Marco de hoja completa
            canvas.rect(20, 20, A4[0]-40, A4[1]-40, fill=0)

            #Fecha del header
            canvas.drawCentredString(A4[0]-100, A4[1]-60, headerDate)
            #Logo del header
            canvas.drawImage(img, 30, A4[1]-90, 60, 60)

            #Footer
            canvas.drawCentredString((A4[0]/2)-3, 50, footer)
            canvas.restoreState()

        #Recupero la orden
        order = Order.objects.get(pk=kwargs['pk'])

        #Declaro el tipo de contenido del response
        response = HttpResponse(content_type='application/pdf')

        buffer = BytesIO()
        pdf_doc = SimpleDocTemplate(buffer, title=f'factura_{order.id}', pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=60)

        #Contenido
        stylesheet = getSampleStyleSheet()
        stylesheet.add(ParagraphStyle(name='Parrafo', fontName ='Helvetica',fontSize=12, leading=16))
        stylesheet.add(ParagraphStyle(name='Footer', fontSize=12, leading=16))
        doc_content = []

        #Título
        style = stylesheet["Title"]
        title = Paragraph('Libreria "The Eye Of Minds"', style)
        doc_content.append(title)

        #Datos personales
        doc_content.append(Spacer(1, 24))
        style = stylesheet['Parrafo']
    
        linea_factura = Paragraph(f'Factura N°: {order.id}', style)
        doc_content.append(linea_factura)
        linea_factura = Paragraph(f'Cliente: {order.c_name}', style)
        doc_content.append(linea_factura)
        linea_factura = Paragraph(f'Email: {order.c_email}', style)
        doc_content.append(linea_factura)
        linea_factura = Paragraph(f'Fecha: {order.date.day}/{order.date.month}/{order.date.year}', style)
        doc_content.append(linea_factura)
        linea_factura = Paragraph(f'Hora: {order.date.hour}:{order.date.minute} hrs', style)
        doc_content.append(linea_factura)

        #Renglones detallados
        renglones = order.orderline_set.all()
        doc_content.append(Spacer(1, 24))
        datos = []
        datos.append(['Libro', 'Precio', 'Cantidad', 'Total'])
        for r in renglones:
            datos.append([f'{r.b_title}', f'${r.b_price}', f'{r.quantity}', f'${r.get_value()}'])
        datos.append(['Total', '', '', f'${order.get_total()}'])

        tabla = Table(datos, colWidths=(350, None, None, None))
        style = TableStyle([
            ('ALIGN', (1,0), (-1,-1), 'CENTER'),
            ('ALIGN', (0,0), (0,-1), 'LEFT'),
            ('BACKGROUND', (0,0), (-1,0), colors.grey),
            ('BACKGROUND', (0,-1), (-1,-1), colors.grey),
            ('FONTSIZE', (0,0), (-1,0), 14),
            ('FONTSIZE', (0,-1), (-1,-1), 14),
            ('FONTSIZE', (0,1), (-1,-1), 12),
            ('BOTTOMPADDING', (0,0), (-1,0), 10),
            ('BOTTOMPADDING', (0,1), (-1,-1), 5),
            ('GRID', (0,0), (-1,-1), 1, colors.black),
        ])
        tabla.setStyle(style)
        doc_content.append(tabla)

        #Creación del documento
        pdf_doc.build(doc_content, onFirstPage=headerFooter, onLaterPages=headerFooter)
        
        response.write(buffer.getvalue())
        buffer.seek(0)

        #Control de seguridad. Si no tiene permitido ver la factura
        #   se lo redirecciona a un templeta de error.
        u_group = request.user.get_group()
        owner = request.user.profile.pk == order.c_profile_pk
        if owner or u_group == 'Administradores' or u_group == 'Gerentes':
            return FileResponse(buffer, as_attachment=True, filename=f'factura_{order.id}.pdf')
        else:
            return super().get(request, *args, **kwargs)