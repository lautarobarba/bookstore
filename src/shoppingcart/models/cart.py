from django.db import models
from market.models import Book
from django.contrib.auth import get_user_model

User = get_user_model()

class Cart(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, through='ProductList')
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        #return '{1} {0}'.format(self.client.profile, 'carrito de ')
        return f'Carrito de {self.client.profile}'

    def get_absolute_url(self):
        return reverse('cart-detail', args=[str(self.id)])


class ProductList(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def get_value(self):
        return self.book.price*self.quantity

     