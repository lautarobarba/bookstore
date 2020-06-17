from django.urls import path
from shoppingcart.views import (
    CartDetailView, add_to_cart, remove_from_cart, 
    OrderCreateView, OrderListView,  OrderDetailView,
    PrintOrderView,
    ResumeView,
)

urlpatterns = [
    path('cartdetail/<int:pk>/', CartDetailView.as_view(), name='cart-detail'),
    path('add-to-cart/<int:pk>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<int:pk>/', remove_from_cart, name='remove-from-cart'),
    path('order/new/', OrderCreateView.as_view(), name='order-new'),
    path('order/list/', OrderListView.as_view(), name='order-list'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('order/print/<int:pk>/', PrintOrderView.as_view(), name='order-print'),
    path('resume/', ResumeView.as_view(), name='resume-list'),
]