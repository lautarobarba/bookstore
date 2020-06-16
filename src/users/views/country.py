from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import Country
from django.urls import reverse_lazy

class CountryCreateView(LoginRequiredMixin, CreateView):
    model = Country
    template_name = 'users/country_create.html'
    fields = '__all__'

class CountryListView(LoginRequiredMixin, ListView):
    model = Country
    queryset = Country.objects.order_by('name')
    paginate_by = 10

class CountryUpdateView(LoginRequiredMixin, UpdateView):
    model = Country
    template_name = 'users/country_update.html'
    fields = '__all__'

class CountryDeleteView(LoginRequiredMixin, DeleteView):
    model = Country
    template_name = 'users/country_delete.html'
    success_url = reverse_lazy('country-list')