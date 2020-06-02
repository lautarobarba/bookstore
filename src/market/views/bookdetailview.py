from django.views.generic.detail import DetailView
from market.models.book import Book 
from django.forms import Form
from django.shortcuts import render
#from carrito.models import Carrito

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