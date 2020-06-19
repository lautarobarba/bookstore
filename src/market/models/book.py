from django.db import models
from .author import Author
from .genre import Genre
from .editorial import Editorial
from .discount import Discount
from django.urls import reverse
from PIL import Image

class Book(models.Model):
    title = models.CharField(verbose_name='título', max_length=255)
    isbn = models.BigIntegerField(unique=True)
    sinopsis = models.CharField(max_length=255)
    price = models.FloatField(verbose_name='precio')
    discount = models.ForeignKey(Discount, verbose_name='descuento', null=True, blank=True, on_delete=models.PROTECT)
    created = models.DateTimeField(verbose_name='creado', auto_now_add=True, null=True)
    cover = models.ImageField(verbose_name='portada', upload_to='book_cover/', default='default-cover.png')
    authors = models.ManyToManyField(Author, verbose_name='autor')
    genres = models.ManyToManyField(Genre, verbose_name='generos')
    editorial = models.ForeignKey(Editorial, verbose_name='editorial', on_delete=models.PROTECT)
    
    
    #pictures = models.ManyToManyField(Genre, verbose_name='generos')

    class Meta():
        ordering = ['title']
        constraints = [
            models.UniqueConstraint(fields=['title', 'editorial'], name='unique title in editorial')
        ]

    def get_price(self):
        if self.discount:
            return self.price - self.price * (self.discount.value / 100)
        else:
            return self.price

    # Modifico el tamaño de la portada antes de guardar
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.cover:
            img = Image.open(self.cover.path)
            if img.height > 400 or img.width > 250:
                img.thumbnail((400, 200))
                img.save(self.cover.path)
        
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
        #return '{0} {1}'.format(self.title, self.editorial)
        return self.title