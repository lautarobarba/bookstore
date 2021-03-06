from django.urls import path
from market.views import (
    HomeView, DashboardView, BookDetailView, GenreListView, BookListView,
    AuthorCreateView, AuthorListView, AuthorUpdateView, AuthorDeleteView,
    EditorialCreateView, EditorialListView, EditorialUpdateView, EditorialDeleteView,
    GenreCreateView, GenreListView, GenreUpdateView, GenreDeleteView,
    DiscountCreateView, DiscountListView, DiscountUpdateView, DiscountDeleteView,
    BookCreateView, BookAdminListView, BookUpdateView, BookDeleteView, BookSearchView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    # Búsquedas de libros
    path('book/all/', BookListView.as_view(), {'type': 'all'}, name='book-list'),
    path('book/on-sale/', BookListView.as_view(), {'type': 'on-sale'}, name='book-on-sale'),
    path('book/search/', BookSearchView.as_view(), name='book-search'),
    path('book/genre/<str:genre>/', BookListView.as_view(), {'type': 'genre'}, name='book-genre-list'),  
    path('book/author/<str:first_name>-<str:last_name>/', BookListView.as_view(), {'type': 'author'} , name='book-author-list'),  
    path('book/editorial/<str:editorial>/', BookListView.as_view(), {'type': 'editorial'} , name='book-editorial-list'),
    ##### DASHBOAR ADMINISTRADORES 
    ## QUITAR NO SE USA - ELIMINAR VIEW Y TEMPLATE
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
    # Genre URLS
    path('genre/', GenreListView.as_view(), name='genre-list'),
    path('genre/new/', GenreCreateView.as_view(), name='genre-new'),
    path('genre/update/<int:pk>', GenreUpdateView.as_view(), name='genre-update'),
    path('genre/delete/<int:pk>', GenreDeleteView.as_view(), name='genre-delete'),
    # Discount URLS
    path('discount/', DiscountListView.as_view(), name='discount-list'),
    path('discount/new/', DiscountCreateView.as_view(), name='discount-new'),
    path('discount/update/<int:pk>', DiscountUpdateView.as_view(), name='discount-update'),
    path('discount/delete/<int:pk>', DiscountDeleteView.as_view(), name='discount-delete'),
    # Book URLS
    path('book/new/', BookCreateView.as_view(), name='book-new'),
    path('book/admin/', BookAdminListView.as_view(), name='book-admin-list'),
    path('book/update/<int:pk>', BookUpdateView.as_view(), name='book-update'),
    path('book/delete/<int:pk>', BookDeleteView.as_view(), name='book-delete'),
]