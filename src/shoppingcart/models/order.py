from django.db import models
from market.models import Book
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, through='OrderLine')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Compra N°: {self.id}. Cliente: {self.client.profile}'
    
    def get_total(self):
        total = 0
        for book in self.orderline_set.all():
            #print(book)
            total += book.get_value()
        return total

    def get_absolute_url(self):
        return reverse('cart-detail', args=[str(sself.client.cart.id)])

class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def get_value(self):
        return self.book.price*self.quantity