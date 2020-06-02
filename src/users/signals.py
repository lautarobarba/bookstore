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



#@receiver(post_save, sender=Profile)
#def edit_profile_picture(sender, instance, created, **kwargs):
    #if instance.picture:
        #print('Este perfil tiene una foto')
        #print(instance.picture.url)
        #img_filename = '..' + instance.picture.url
        #print(img_filename)
        #with Image.open(img_filename) as img:
            #print(img.size)

            #if (img.height > 300) or (img.width > 300):
                #print('Se edito el tamaño de la imagen')
                #img.thumbnail((300, 300))
                #img.save(img_filename)

            #print(img.size)


@receiver(post_save, sender=Profile)
def asign_group(sender, instance, created, **kwargs):
    if instance.group == None:
        if instance.user.is_superuser:
            admin_group = None
            try: 
                admin_group = Group.objects.get(name='admin')
            except:
                # If admin group does not exist
                admin_group = Group(name='admin')
                admin_group.save()
            finally:
                instance.group = admin_group
                instance.save()
        else:
            user_group = None
            try: 
                user_group = Group.objects.get(name='user')
            except:
                # If user group does not exist
                user_group = Group(name='user')
                user_group.save()
            finally:
                instance.group = user_group
                instance.save()