from django.urls import path
from shoppingcart.views import CartDetailView, add_to_cart, remove_from_cart

urlpatterns = [
    path('cartdetail/<int:pk>/', CartDetailView.as_view(), name='cart-detail'),
    path('add-to-cart/<int:pk>', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<int:pk>', remove_from_cart, name='remove-from-cart'),
]