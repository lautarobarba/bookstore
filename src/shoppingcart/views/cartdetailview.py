from django.views.generic.detail import DetailView
from shoppingcart.models import Cart
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import CartOwnerMixin

class CartDetailView(CartOwnerMixin, LoginRequiredMixin, DetailView):
    model = Cart

    #login_url = '/users/login/'

    #def get(self, request, *args, **kwargs):
     #   self.cart_id = request.user.cart.id
      #  print(self.cart_id)
       # return super().get(request, *args, **kwargs)

    #def get_object(self):
     #   return Cart.objects.get(id=self.cart_id)