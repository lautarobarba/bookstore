from django.db import models
from django.shortcuts import reverse
from market.models.validators import StringWithoutSlashValidator

class Country(models.Model):
    name = models.CharField(verbose_name='nombre', max_length=255, unique=True, validators=[StringWithoutSlashValidator])

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('country-list')

    class Meta:
        verbose_name = 'país'
        verbose_name_plural = "países"