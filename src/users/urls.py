from django.urls import path
from .views import (
    UserCreateView, UserLoginView, UserLogoutView, UserDeleteView,
    ProfileDetailView, ProfileUpdateView,
    CountryListView, CountryCreateView, CountryUpdateView, CountryDeleteView,
)

urlpatterns = [
    path('new/', UserCreateView.as_view(), name='user-new'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/update/<int:pk>/', ProfileUpdateView.as_view(), name='profile-update'),
    path('country/', CountryListView.as_view(), name='country-list'),
    path('country/new/', CountryCreateView.as_view(), name='country-new'),
    path('country/update/<int:pk>', CountryUpdateView.as_view(), name='country-update'),
    path('country/delete/<int:pk>', CountryDeleteView.as_view(), name='country-delete'),
]