from django.shortcuts import render
from wishlist.mixins import WishlistOwnerMixin
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, redirect
from market.models import Book
from wishlist.models import Wishlist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

class WishlistDetailView(WishlistOwnerMixin, LoginRequiredMixin, ListView):
    model = Wishlist 
    template_name = 'wishlist/wishlist_list.html'

    def get_queryset(self, **kwargs):
        list = Wishlist.objects.get(pk = self.kwargs['pk']).books.all()
        #print(list)
        return list

@login_required
def add_to_wishlist(request, pk):
    book = get_object_or_404(Book, pk = pk)
    wishlist = request.user.wishlist

    wishlist.books.add(book)

    return redirect('/')

@login_required
def remove_from_wishlist(request, pk):
    book = get_object_or_404(Book, pk = pk)
    wishlist = request.user.wishlist

    wishlist.books.remove(book)

    return redirect(wishlist.get_absolute_url())


