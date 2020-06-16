from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.urls import reverse
from .country import Country
from PIL import Image

# User set in global settings
User = get_user_model()

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    first_name = models.CharField(verbose_name='nombre', max_length=255, null=True, blank=True)
    last_name = models.CharField(verbose_name='apellido', max_length=255, null=True, blank=True)
    country = models.ForeignKey(Country, verbose_name='país', null=True, blank=True, on_delete=models.SET_NULL)
    phone = models.CharField(verbose_name='teléfono', max_length=12, null=True, blank=True)
    picture = models.ImageField(verbose_name='foto de perfil', upload_to='users/', default='default.jpg')

    # Role
    # Add default "user" group
    group = models.ForeignKey(Group, verbose_name='grupo', null=True, blank=True, on_delete=models.SET_NULL)


    # Modifico el save para que redimensione la imagen antes de guardar
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.picture:
            img = Image.open(self.picture.path)
            if img.height > 300 or img.width > 300:
                img.thumbnail((300, 300))
                super().save(*args, **kwargs)
        

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return f'{self.user.email}'

    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'pk':self.pk})