from django.urls import path
from market.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]