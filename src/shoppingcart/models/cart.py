from django.db import models
from market.models import Book
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Cart(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, through='ProductList')

    def __str__(self):
        return f'Carrito de {self.client.profile}'

    def get_absolute_url(self):
        return reverse('cart-detail', args=[str(self.id)])

    def get_total(self):
        total = 0
        for book in self.productlist_set.all():
            #print(book)
            total += book.get_value()
        return total

    def is_empty(self):
        if len(self.productlist_set.all()) == 0:
            return True
        else:
            return False

class ProductList(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def get_value(self):
        return self.book.get_price()*self.quantity