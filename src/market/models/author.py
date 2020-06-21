from django.db import models
from django.urls import reverse
from .validators import StringWithoutSlashValidator

class Author(models.Model):
    first_name = models.CharField(verbose_name='nombre', max_length=255, validators=[StringWithoutSlashValidator])
    last_name = models.CharField(verbose_name='apellido', max_length=255, validators=[StringWithoutSlashValidator])

    class Meta():
        ordering = ['first_name', 'last_name']
        unique_together = [['first_name', 'last_name']]
        verbose_name = "autor"
        verbose_name_plural = "autores"

    def __str__(self):
        fullname = '{0} {1}'.format(self.first_name, self.last_name)
        return fullname
    
    def save(self, *args, **kwargs):
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('author-list')