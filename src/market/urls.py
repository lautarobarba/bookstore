from django.urls import path
from market.views import HomeView, DashboardView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-view'),
    path('genres/', GenreListView.as_view(), name='genre-list-view'),
    path('genres/<slug:slug>/', BookListView.as_view(), name='book-list-view'),  
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]