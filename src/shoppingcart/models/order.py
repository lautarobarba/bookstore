from django.db import models
from market.models import Book
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    #Datos del cliente
    c_name = models.CharField(verbose_name='cliente', max_length=210)
    c_email = models.EmailField(verbose_name='email')
    c_profile_pk = models.IntegerField(default=0)

    def __str__(self):
        return f'Compra N°: {self.id}. Cliente: {self.c_name}'
    
    def get_total(self):
        total = 0
        #Recupero todas las lineas de la orde
        lineas = OrderLine.objects.filter(order=self)
        for l in lineas:
            total += l.get_value()
        return total

    def get_absolute_url(self):
        return reverse('order-detail', kwargs={'pk':self.pk})

class OrderLine(models.Model):
    #A que orden pertenece
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    #Datos del libro
    b_title = models.CharField(verbose_name='libro', max_length=255)
    b_editorial = models.CharField(verbose_name='editorial', max_length=255)
    b_price = models.FloatField(verbose_name='precio')
    b_pk = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

    def get_value(self):
        return self.b_price * self.quantity