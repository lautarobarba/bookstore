from django.views.generic.detail import DetailView
from shoppingcart.models import Cart

class CartDetailView(DetailView):
    model = Cart