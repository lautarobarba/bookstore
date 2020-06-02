from django.db import models
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length=255)

    class Meta():
        ordering = ['name']
    
    #def get_absolute_url(self):
        #return reverse('', args=[str(self.id)])

    def __str__(self):
        return self.name