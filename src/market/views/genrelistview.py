from django.views.generic import ListView
from libreria.models.genre import Genre

class GenreListView(ListView):
    model = Genre