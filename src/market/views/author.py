from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from market.models import Author
from django.urls import reverse_lazy

class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    template_name = 'market/author_create.html'
    fields = '__all__'

class AuthorListView(ListView):
    model = Author
    queryset = Author.objects.order_by('first_name', 'last_name')
    paginate_by = 10

class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    model = Author
    template_name = 'market/author_update.html'
    fields = '__all__'

class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author
    template_name = 'market/author_delete.html'
    success_url = reverse_lazy('author-list')