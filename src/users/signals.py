from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from users.models import Profile


#from PIL import Image
#from blog.settings import BASE_DIR
#import os

from django.contrib.auth.models import Group

User = get_user_model()

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()

@receiver(post_save, sender=Profile)
def asign_group(sender, instance, created, **kwargs):
    if instance.group == None:
        if instance.user.is_superuser:
            admin_group, status = Group.objects.get_or_create(name='admin')
            instance.group = admin_group
            instance.save()
        else:
            user_group, status = Group.objects.get_or_create(name='user')
            instance.group = user_group
            instance.save()