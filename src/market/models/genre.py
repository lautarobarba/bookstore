from django.db import models
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(verbose_name='nombre', max_length=255, unique=True)

    class Meta():
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('genre-list')