from django.views.generic import ListView
from market.models.genre import Genre

class GenreListView(ListView):
    model = Genre