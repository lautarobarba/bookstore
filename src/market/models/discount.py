from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from .validators import DiscountValidator

class Discount(models.Model):
    value = models.IntegerField(verbose_name='valor', unique=True, validators=[MinValueValidator(1), MaxValueValidator(99), DiscountValidator])

    class Meta():
        ordering = ['value']

    def __str__(self):
        return f'{self.value}%'

    def get_absolute_url(self):
        return reverse('discount-list')

    class Meta:
        verbose_name = "descuento"
        verbose_name_plural = "descuentos"