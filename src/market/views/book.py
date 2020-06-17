from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.forms import Form
from django.contrib.auth.mixins import LoginRequiredMixin
from market.models import Book
from django.urls import reverse_lazy
from shoppingcart.models import ProductList
from django.shortcuts import redirect,render

# Objetos usados en BookSearchView
from market.models import Genre, Editorial, Author

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'market/book_create.html'
    fields = '__all__'

class BookAdminListView(LoginRequiredMixin, ListView):
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
            queryset =  Book.objects.filter(genres__name__icontains=self.genre)
        elif self.type == 'author':
            queryset = Book.objects.filter(authors__first_name__icontains=self.author_first_name, authors__last_name__icontains=self.author_last_name)
        elif self.type == 'editorial':
            queryset = Book.objects.filter(editorial__name__icontains=self.editorial)
        elif self.type == 'on-sale':
            queryset = Book.objects.exclude(sale=None)
        else:
            queryset = Book.objects.all()
        return queryset 

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'market/book_update.html'
    fields = '__all__'

class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'market/book_delete.html'
    success_url = reverse_lazy('book-admin-list')

class BookDetailView(DetailView):
    model = Book
    form_class = Form
    template_name = 'market/book_detail.html'

class BookSearchView(ListView):
    model = Book 
    form_class = Form
    template_name = 'market/book_search_list.html'
    paginate_by = 10
    
    def get(self, request, *args, **kwargs):
        try:
            self.title = request.GET.get('title')
        except:
            self.title = None
        if request.GET.get('author') == 'Autor...':
            self.author = None
        else:
            self.author = request.GET.get('author')
        if request.GET.get('genre') == 'Género...':
            self.genre = None
        else:
            self.genre = request.GET.get('genre') 
        if request.GET.get('editorial') == 'Editorial...':
            self.editorial = None
        else:
            self.editorial = request.GET.get('editorial')          
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Book.objects.all()
        if self.title or self.author or self.genre or self.editorial:
            if self.title:
                queryset =  queryset.filter(title__icontains=self.title)
            if self.author:
                a_first_name = self.author.split()[0]
                a_last_name = self.author.split()[1]
                queryset =  queryset.filter(authors__first_name__icontains=a_first_name, authors__last_name__icontains=a_last_name)
            if self.genre:
                queryset =  queryset.filter(genres__name__icontains=self.genre)
            if self.editorial:
                queryset =  queryset.filter(editorial__name__icontains=self.editorial)
        else:
            queryset = queryset.filter(title='')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['generos'] = Genre.objects.all()
        context['editoriales'] = Editorial.objects.all()
        context['autores'] = Author.objects.all()
        return context