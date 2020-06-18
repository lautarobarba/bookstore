from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from shoppingcart.models import Order, OrderLine, ProductList 
from django.views.generic import ListView
from django.views import View
from django.forms import Form
from datetime import datetime

### Necesario para hacer los pdfs
import io
from django.http import FileResponse
from django.template.loader import get_template

#from reportlab.pdfgen import canvas
#from reportlab.lib.pagesizes import A4

#import itertools

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
        lineas = ProductList.objects.filter(cart=u_cart)

        #Creo una nueva compra
        new_order = Order(client=u_client)
        new_order.save()

        #Guardo los libros del carrito en la compra
        for l in lineas:
            new_l = OrderLine(order=new_order, book=l.book, quantity=l.quantity)
            new_l.save()
            #Elimino los libros del carrito
            l.delete()
        return redirect(new_order)

class OrderListView(ListView):
    model = Order
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.client = request.user
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
            return Order.objects.filter(client=self.client)

class OrderDetailView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'shoppingcart/order_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = Order.objects.get(pk=self.kwargs['pk'])
        context['order'] = order
        context['productos'] = order.orderline_set.all()
        context['total'] = order.get_total()
        context['owner'] = order.client.id
        return context

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
        order = Order.objects.get(pk=self.kwargs['pk'])
        products = order.orderline_set.all()

        data = dict()
        data['order'] = order 
        data['productos'] = order.orderline_set.all()
        data['total'] = order.get_total()
        data['owner'] = order.client.id

        #PASAR EL USUARIO Y EL GRUPO LOGUEADO PARA SEGURIDAD DENTRO DEL TEMPLATE

        template = get_template(self.template_name)
        #Le paso todos los datos del contexto capturados en ge_context_data
        html  = template.render(data)
        buffer = io.BytesIO()
        pdf = pisa.pisaDocument(io.BytesIO(html.encode("utf-8")), buffer)

        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename=f'Factura_{order.id}.pdf')