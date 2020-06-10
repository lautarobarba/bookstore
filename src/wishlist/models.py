from django.db import models
from market.models import Book
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Wishlist(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return f'Lista de deseados de {self.client.profile}'

    def get_absolute_url(self):
        return reverse('wishlist-list', args=[str(self.id)])

    