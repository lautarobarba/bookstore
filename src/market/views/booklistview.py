from django.views.generic import ListView
from market.models.book import Book, Genre

class BookListView(ListView):
    model = Book 
    #template_name = 'libreria/'

    def get(self, request, *args, **kwargs):
        nombre_genero = self.kwargs['slug']
        genero_obj = Genre.objects.get(name=nombre_genero)
        self.genero_id = genero_obj.id
        #print('Genero id: ')
        #print(self.genero_id)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genero_id'] = self.genero_id
        return context

    def get_queryset(self):
        return Book.objects.filter(genres=self.genero_id)#[:5]