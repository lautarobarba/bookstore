from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from shoppingcart.models import Order, OrderLine, ProductList
from django.forms import Form   

class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    template_name = 'shoppingcart/order_create.html'
    fields = '__all__'

    def post(self, request, *args, **kwargs):
        u_client = request.user
        u_cart = request.user.cart
        #print(u_cart.books.all())
        lineas = ProductList.objects.filter(cart=u_cart)

        #Creo una nueva orden con el cliente y timestamp actual
        new_order = Order(client=u_client)
        new_order.save()

        #Guardo los libros del carrito en la compra
        for l in lineas:
            new_l = OrderLine(order=new_order, book=l.book, quantity=l.quantity)
            new_l.save()
            l.delete()

        #print(new_order.books.all())
        return redirect('home')