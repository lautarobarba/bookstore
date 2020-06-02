from django.db import models
from django.shortcuts import reverse

class Country(models.Model):
    name = models.CharField(verbose_name='país', max_length=255, unique=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('country-list')