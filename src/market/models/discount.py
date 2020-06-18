from django.db import models
from django.urls import reverse

class Discount(models.Model):
    name = models.IntegerField(verbose_name='descuento')

    class Meta():
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('discount-list')