from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from market.models import Editorial
from django.urls import reverse_lazy

# Custom mixins
from users.views.mixins import GroupContextMixin

class EditorialCreateView(GroupContextMixin, LoginRequiredMixin, CreateView):
    model = Editorial
    template_name = 'market/editorial_create.html'
    fields = '__all__'

class EditorialListView(GroupContextMixin, LoginRequiredMixin, ListView):
    model = Editorial
    queryset = Editorial.objects.order_by('name')

class EditorialUpdateView(GroupContextMixin, LoginRequiredMixin, UpdateView):
    model = Editorial
    template_name = 'market/editorial_update.html'
    fields = '__all__'

class EditorialDeleteView(GroupContextMixin, LoginRequiredMixin, DeleteView):
    model = Editorial
    template_name = 'market/editorial_delete.html'
    success_url = reverse_lazy('editorial-list')