from django.shortcuts import get_object_or_404, redirect
from market.models import Book
from shoppingcart.models import ProductList
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, pk):
    book = get_object_or_404(Book, pk = pk)
    cart = request.user.cart

    o, status = ProductList.objects.get_or_create(cart = cart, book = book)
    o.quantity += 1
    o.save()

    wishlist = request.user.wishlist
    #print(book)
    #print(wishlist.books.get(pk = pk))
    try:
        book = wishlist.books.get(pk = pk)
        wishlist.books.remove(book)
    except(Book.DoesNotExist):
        print("Ese libro no existe en la wishlist")

    if(status):    
        return redirect(book.get_absolute_url())
    else:
        return redirect(cart.get_absolute_url())

@login_required
def remove_from_cart(request, pk):
    book = get_object_or_404(Book, pk = pk)
    cart = request.user.cart

    o, status = ProductList.objects.get_or_create(cart = cart, book = book)

    if not(status):
        if(o.quantity == 1):
            cart.books.remove(book)
        else:
            o.quantity -= 1
            o.save()

    return redirect(cart.get_absolute_url())