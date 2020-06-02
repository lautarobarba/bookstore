from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import Country
from django.urls import reverse_lazy

# Custom mixins
from .mixins import GroupContextMixin

class CountryCreateView(GroupContextMixin, LoginRequiredMixin, CreateView):
    model = Country
    template_name = 'users/country_create.html'
    fields = '__all__'

class CountryListView(GroupContextMixin, LoginRequiredMixin, ListView):
    model = Country
    queryset = Country.objects.order_by('name')

class CountryUpdateView(GroupContextMixin, LoginRequiredMixin, UpdateView):
    model = Country
    template_name = 'users/country_update.html'
    fields = '__all__'

class CountryDeleteView(GroupContextMixin, LoginRequiredMixin, DeleteView):
    model = Country
    template_name = 'users/country_delete.html'
    success_url = reverse_lazy('country-list')