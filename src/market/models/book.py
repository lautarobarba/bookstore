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

    title = models.CharField(verbose_name='título', max_length=255)
    isbn = models.BigIntegerField(unique=True)
    sinopsis = models.CharField(max_length=255)
    price = models.FloatField(verbose_name='precio')
    sale = models.CharField(verbose_name='promoción', max_length=1 ,choices=SALE_CHOICES, null=True, blank=True)
    created = models.DateTimeField(verbose_name='creado', auto_now_add=True, null=True)
    #Relations
    authors = models.ManyToManyField(Author, verbose_name='autor')
    editorial = models.ForeignKey(Editorial, verbose_name='editorial', on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre, verbose_name='generos')
    cover = models.ImageField(verbose_name='portada', upload_to='book_cover/', null=True, blank=True)
    
    #pictures = models.ManyToManyField(Genre, verbose_name='generos')

    class Meta():
        ordering = ['title']
        constraints = [
            models.UniqueConstraint(fields=['title', 'editorial'], name='unique title in editorial')
        ]

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def get_add_to_wishlist(self):
        return reverse('add-to-wishlist', args=[str(self.id)])

    def get_remove_from_wishlist(self):
        return reverse('remove-from-wishlist', args=[str(self.id)])

    def get_add_to_cart(self):
        return reverse('add-to-cart', args=[str(self.id)])

    def get_remove_from_cart(self):
        return reverse('remove-from-cart', args=[str(self.id)])

    def __str__(self):
        return '{0} {1}'.format(self.title, self.editorial)