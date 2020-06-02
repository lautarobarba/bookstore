from django.contrib import admin
from users.models import User, Profile, Country

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Country)