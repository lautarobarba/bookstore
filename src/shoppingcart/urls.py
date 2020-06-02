from django.urls import path
from shoppingcart.views import CartDetailView

urlpatterns = [
    path('cartdetail/', CartDetailView.as_view(), name='cart-detail')
]