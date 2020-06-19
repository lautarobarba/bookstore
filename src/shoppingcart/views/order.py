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
#from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate
#import itertools
from django.http import HttpResponse
from xhtml2pdf import pisa
###


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
            new_order.c_name = u_client.profile.first_name + u_client.profile.last_name
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

class PrintOrderView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'shoppingcart/order_print.html'

    def get(self, request, *args, **kwargs):
        #Recupero la orden
        
        # declaro el tipo de contenido del response
        pdf_name = 'nombre.pdf'
        response = HttpResponse(content_type='application/pdf')
        # nombre del archivo que va a ser devuelto
        #response['Content-Disposition'] = f'attachment; filename="{pdf_name}"'
        buffer = BytesIO()
        pdf_doc = SimpleDocTemplate(buffer, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)

        doc_content = []
        #Contenido
        styles = getSampleStyleSheet()
        title_style = styles["Title"]
        title = Paragraph('Hola Mundo', title_style)
        doc_content.append(title)

        pdf_doc.build(doc_content)
        response.write(buffer.getvalue())
        #buffer.close()
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='hello.pdf')