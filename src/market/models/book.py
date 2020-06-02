from django.db import models
from .author import Author
from .genre import Genre
from .editorial import Editorial
from django.urls import reverse

class Book(models.Model):

    SALE_CHOICES = [
        ('C', '5%'),
        ('D', '10%'),
        ('Q', '15%'),
        ('V', '20%'),
    ]

    title = models.CharField(max_length=255)
    isbn = models.BigIntegerField(unique=True)
    sinopsis = models.CharField(max_length=255)
    price = models.FloatField()
    sale = models.CharField(max_length=1 ,choices=SALE_CHOICES, null=True, blank=True)
    authors = models.ManyToManyField(Author)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre)
    #photo = 

    class Meta():
        ordering = ['title']
        constraints = [
            models.UniqueConstraint(fields=['title', 'editorial'], name='unique title in editorial')
        ]

    def get_absolute_url(self):
        return reverse('book-view', args=[str(self.id)])

    def __str__(self):
        return '{0} {1}'.format(self.title, self.editorial)
    
     