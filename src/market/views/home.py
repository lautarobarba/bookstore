from django.views.generic import ListView
from market.models import Book

class HomeView(ListView):
    template_name = 'market/home.html'
    model = Book 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_list_sale'] = Book.objects.exclude(sale=None)[:8]
        return context
    
    def get_queryset(self):
        return Book.objects.all().order_by('created')[:8]