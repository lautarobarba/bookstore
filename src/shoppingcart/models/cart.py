from django.db import models
from market.models import Book
from django.contrib.auth import get_user_model

User = get_user_model()

class Cart(models.Model):
    client = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Book)
    last_updated = models.DateTimeField(auto_now=True)