from django.urls import path
from market.views import (
    HomeView, DashboardView, BookDetailView, GenreListView, BookListView,
    AuthorCreateView, AuthorListView, AuthorUpdateView, AuthorDeleteView,
    EditorialCreateView, EditorialListView, EditorialUpdateView, EditorialDeleteView,
    GenreCreateView, GenreListView, GenreUpdateView, GenreDeleteView,
    BookCreateView, BookAdminListView, BookUpdateView, BookDeleteView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-view'),
    path('genres/', GenreListView.as_view(), name='genre-list-view'),
    path('genres/<slug:slug>/', BookListView.as_view(), name='book-list-view'),  
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # Author URLS
    path('author/', AuthorListView.as_view(), name='author-list'),
    path('author/new/', AuthorCreateView.as_view(), name='author-new'),
    path('author/update/<int:pk>', AuthorUpdateView.as_view(), name='author-update'),
    path('author/delete/<int:pk>', AuthorDeleteView.as_view(), name='author-delete'),
    # Editorial URLS
    path('editorial/', EditorialListView.as_view(), name='editorial-list'),
    path('editorial/new/', EditorialCreateView.as_view(), name='editorial-new'),
    path('editorial/update/<int:pk>', EditorialUpdateView.as_view(), name='editorial-update'),
    path('editorial/delete/<int:pk>', EditorialDeleteView.as_view(), name='editorial-delete'),
    # Gente URLS
    path('genre/', GenreListView.as_view(), name='genre-list'),
    path('genre/new/', GenreCreateView.as_view(), name='genre-new'),
    path('genre/update/<int:pk>', GenreUpdateView.as_view(), name='genre-update'),
    path('genre/delete/<int:pk>', GenreDeleteView.as_view(), name='genre-delete'),
    # Book URLS
    path('book/new/', BookCreateView.as_view(), name='book-new'),
    path('book/admin/', BookAdminListView.as_view(), name='book-admin-list'),
    path('book/update/<int:pk>', BookUpdateView.as_view(), name='book-update'),
    path('book/delete/<int:pk>', BookDeleteView.as_view(), name='book-delete'),
]