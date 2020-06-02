from django.db import models
from django.urls import reverse

class Author(models.Model):
    first_name = models.CharField(verbose_name='nombre', max_length=255)
    last_name = models.CharField(verbose_name='apellido', max_length=255)

    class Meta():
        ordering = ['last_name']

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('author-list')