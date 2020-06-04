from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.forms import Form
from django.contrib.auth.mixins import LoginRequiredMixin
from market.models import Book
from django.urls import reverse_lazy

# Custom mixins
from users.views.mixins import GroupContextMixin

class BookCreateView(GroupContextMixin, LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'market/book_create.html'
    fields = '__all__'

class BookAdminListView(GroupContextMixin, LoginRequiredMixin, ListView):
    model = Book
    template_name = 'market/book_admin_list.html'
    queryset = Book.objects.order_by('title')

class BookListView(ListView):
    model = Book 

    def get(self, request, *args, **kwargs):
        self.type = self.kwargs['type']
        if self.type == 'genre':
            self.genre = self.kwargs['genre']
        elif self.type == 'author':
            self.author_first_name = self.kwargs['first_name']
            self.author_last_name = self.kwargs['last_name']
        elif self.type == 'editorial':
            self.editorial = self.kwargs['editorial'] 
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        if self.type == 'genre':
            return Book.objects.filter(genres__name__icontains=self.genre)
        elif self.type == 'author':
            return Book.objects.filter(authors__first_name__icontains=self.author_first_name, authors__last_name__icontains=self.author_last_name)
        elif self.type == 'editorial':
            return Book.objects.filter(editorial__name__icontains=self.editorial)
        else:
            return Book.objects.all()

class BookUpdateView(GroupContextMixin, LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'market/book_update.html'
    fields = '__all__'

class BookDeleteView(GroupContextMixin, LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'market/book_delete.html'
    success_url = reverse_lazy('book-admin-list')

class BookDetailView(DetailView):
    model = Book
    form_class = Form
    template_name = 'market/book_detail.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            book_id = self.kwargs['pk']
            book = Book.objects.get(id=book_id)

            cart = request.user.cart

            #cart.books.add(book, quantity=)

            return render(request, self.template_name, {'form': form})
        else:
            return render(request, self.template_name, {'form': form})