from django.views.generic.detail import DetailView
from django.views.generic import ListView
from shoppingcart.models import Cart, ProductList
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import CartOwnerMixin

class CartDetailView(CartOwnerMixin, LoginRequiredMixin, ListView):
    model = ProductList
    template_name = 'shoppingcart/cart_detail.html'

    def get_queryset(self):
        return ProductList.objects.filter(cart__id = self.kwargs['pk'])

    #login_url = '/users/login/'

    #def get(self, request, *args, **kwargs):
     #   self.cart_id = request.user.cart.id
      #  print(self.cart_id)
       # return super().get(request, *args, **kwargs)

    #def get_object(self):
     #   return Cart.objects.get(id=self.cart_id)