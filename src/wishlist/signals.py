from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from wishlist.models import Wishlist

User = get_user_model()

@receiver(post_save, sender=User)
def create_wishlist(sender, instance, created, **kwargs):
    if created:
        wishlist = Wishlist(client=instance)
        wishlist.save()
    