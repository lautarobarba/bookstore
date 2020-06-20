from django.db import models
from django.urls import reverse
from .validators import StringWithoutSlashValidator

class Genre(models.Model):
    name = models.CharField(verbose_name='nombre', max_length=255, unique=True, validators=[StringWithoutSlashValidator])

    class Meta():
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('genre-list')