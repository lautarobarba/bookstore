from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import Profile
from django.contrib.auth.models import Group

# Custom User
from django.contrib.auth import get_user_model
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
            # Grupos extra que se crean junto al primer Administrador
            extra_group, status = Group.objects.get_or_create(name='Gestores')
            extra_group, status = Group.objects.get_or_create(name='Gerentes')
            
            admin_group, status = Group.objects.get_or_create(name='Administradores')
            instance.group = admin_group
            instance.save()
        else:
            user_group, status = Group.objects.get_or_create(name='Clientes')
            instance.group = user_group
            instance.save()