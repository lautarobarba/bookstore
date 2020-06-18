from django.views.generic.edit import CreateView, DeleteView
from users.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from users.models import Profile
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

# Custom mixins
from .mixins import ProfileOwnerMixin

# Custom User
from django.contrib.auth import get_user_model
User = get_user_model()

class UserCreateView(CreateView):
    model = User
    template_name = 'users/user_create.html'
    form_class = UserCreationForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            login(request, new_user)
            return redirect(new_user)
        else:
            return render(request, 'users/user_create.html', {'form': form})

class UserLoginView(LoginView):
    template_name = 'users/user_login.html'

class UserLogoutView(LogoutView):
    template_name = 'users/user_logout.html'

class UserDeleteView(LoginRequiredMixin, ProfileOwnerMixin, DeleteView):
    model = User
    template_name = 'users/user_delete.html'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        self.user_logged = request.user
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_logged'] = self.user_logged
        return context

class UserListView(LoginRequiredMixin, ListView):
    model = User
    queryset = User.objects.all()
    paginate_by = 10