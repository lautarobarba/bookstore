from .home import HomeView
from .dashboard import DashboardView
from .author import AuthorCreateView, AuthorListView, AuthorUpdateView, AuthorDeleteView
from .editorial import EditorialCreateView, EditorialListView, EditorialUpdateView, EditorialDeleteView
from .genre import GenreCreateView, GenreListView, GenreUpdateView, GenreDeleteView
from .discount import DiscountCreateView, DiscountListView, DiscountUpdateView, DiscountDeleteView
from .book import (
    BookCreateView, BookAdminListView, BookListView, BookUpdateView, BookDeleteView, BookDetailView, BookSearchView
)
