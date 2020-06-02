from django.views.generic import DetailView
from users.models import Profile
from django.views.generic.edit import UpdateView

# Custom mixins
from .mixins import ProfileOwnerMixin

# Custom User
from django.contrib.auth import get_user_model
User = get_user_model()

class ProfileDetailView(ProfileOwnerMixin, DetailView):
    model = Profile

class ProfileUpdateView(ProfileOwnerMixin, UpdateView):
    model = Profile
    template_name = 'users/profile_update.html'
    fields = ['first_name', 'last_name', 'country', 'phone', 'picture']