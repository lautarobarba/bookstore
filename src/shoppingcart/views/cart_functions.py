from django.shortcuts import get_object_or_404, redirect
from market.models import Book
from shoppingcart.models import ProductList

def add_to_cart(request, pk):
    book = get_object_or_404(Book, pk = pk)
    cart = request.user.cart

    o, status = ProductList.objects.get_or_create(cart = cart, book = book)
    o.quantity += 1
    o.save()

    return redirect('home')

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

    return redirect('home')