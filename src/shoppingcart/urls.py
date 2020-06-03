from django.urls import path
from shoppingcart.views import CartDetailView

urlpatterns = [
    path('cartdetail/<int:pk>/', CartDetailView.as_view(), name='cart-detail')
]