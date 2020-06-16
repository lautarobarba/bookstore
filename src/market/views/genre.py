from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from market.models import Genre
from django.urls import reverse_lazy

class GenreCreateView(LoginRequiredMixin, CreateView):
    model = Genre
    template_name = 'market/genre_create.html'
    fields = '__all__'

class GenreListView(ListView):
    model = Genre
    queryset = Genre.objects.order_by('name')
    paginate_by = 10

class GenreUpdateView(LoginRequiredMixin, UpdateView):
    model = Genre
    template_name = 'market/genre_update.html'
    fields = '__all__'

class GenreDeleteView(LoginRequiredMixin, DeleteView):
    model = Genre
    template_name = 'market/genre_delete.html'
    success_url = reverse_lazy('genre-list')