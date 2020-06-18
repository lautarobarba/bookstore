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
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import itertools
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
        return redirect('home')

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

class PrintOrderView(View):
    template_name = 'shoppingcart/order_print.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = Order.objects.get(pk=self.kwargs['pk'])
        context['order'] = order
        return context

    def get(self, request, *args, **kwargs):
        #Recupero la orden
        order = Order.objects.get(pk=self.kwargs['pk'])
        products = order.orderline_set.all()

        #ACA HAY QUE ARMAR EL PDF DE ALGUNA MANERA MÁGICA
        #p.drawString(100, 100, order.id)
        data = [("Producto", "Cantidad", "Precio")]
        for product in products:
            quantity = product.quantity
            price = product.book.price
            data.append((f"{product.book}", quantity, price))

        buffer = io.BytesIO()
        #p = export_to_pdf(data)
        #p.drawString(100, 100, f"Total: {order.get_total}")
        c = canvas.Canvas(buffer, pagesize=A4)
        w, h = A4
        c.drawString(100, 100, "factura")
        max_rows_per_page = 45
        # Margin.
        x_offset = 50
        y_offset = 50
        # Space between rows.
        padding = 15
        
        xlist = [x + x_offset for x in [0, 200, 250, 300, 350, 400, 480]]
        ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]
        
        args = [iter(data)] * max_rows_per_page
        grouper = itertools.zip_longest(*args)

        for rows in grouper:
            rows = tuple(filter(bool, rows))
            c.grid(xlist, ylist[:len(rows) + 1])
            for y, row in zip(ylist[:-1], rows):
                for x, cell in zip(xlist, row):
                    c.drawString(x + 2, y - padding + 3, str(cell))
            c.showPage()
        #################################################

        # Close the PDF object cleanly, and we're done.
        #c.showPage()
        c.save()

        # FileResponse sets the Content-Disposition header so that browsers
        # present the option to save the file.
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename=f'Factura_{order.id}.pdf')