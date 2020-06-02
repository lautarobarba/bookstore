from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from market.models import Book
from django.urls import reverse_lazy

# Custom mixins
from users.views.mixins import GroupContextMixin

class BookCreateView(GroupContextMixin, LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'market/book_create.html'
    fields = '__all__'