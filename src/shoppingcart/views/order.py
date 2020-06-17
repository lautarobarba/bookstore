from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from shoppingcart.models import Order, OrderLine, ProductList 
from django.views.generic import ListView
from django.forms import Form
from datetime import datetime

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
        try:
            self.day = request.GET.get('day')
        except:
            self.day = None
        try:
            self.month = request.GET.get('month')
        except:
            self.month = None
        try:
            self.year = request.GET.get('year')
        except:
            self.year = None
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Order.objects.all()
        if self.day or self.month or self.year:
            if self.day:
                queryset =  queryset.filter(date__day=self.day)
            if self.month:
                queryset =  queryset.filter(date__month=self.month)
            if self.year:
                queryset =  queryset.filter(date___year=self.year)
        else:
            queryset = queryset.filter(date__year=datetime.now().year, date__month=datetime.now().month, date__day=datetime.now().day)
        return queryset
