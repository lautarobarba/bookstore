from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

class Discount(models.Model):
    value = models.IntegerField(verbose_name='descuento', validators=[MinValueValidator(1), MaxValueValidator(99)])

    class Meta():
        ordering = ['value']

    def __str__(self):
        return f'{self.value}%'

    def get_absolute_url(self):
        return reverse('discount-list')