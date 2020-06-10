from django.urls import path
from wishlist.views import WishlistDetailView, add_to_wishlist

urlpatterns = [
    path('wishlist/<int:pk>', WishlistDetailView.as_view(), name='wishlist-list'),
    path('add-to-wishlist/<int:pk>', add_to_wishlist, name='add-to-cart'),
]