from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from shoppingcart.models import Cart

User = get_user_model()

@receiver(post_save, sender=User)
def create_cart(sender, instance, created, **kwargs):
    if created:
        cart = Cart(client=instance)
        cart.save()
    