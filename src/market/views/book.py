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
            print(book)
            #Con el request.user.carrito
            #carrito = request.user.carrito
            #carrito = Carrito.objects.get(id=carrito_id)
            print('Carrito: ')
            print(carrito.id)
            #carrito.productos.add(book)
            #Hacer relacion

            #return HttpResponseRedirect('/success/')
            return render(request, self.template_name, {'form': form})
            #return libro
        else:
            return render(request, self.template_name, {'form': form})