from django.views.generic import ListView
from shoppingcart.models.Order import Order 
from django.contrib.auth.mixins import LoginRequiredMixin

class ResumeView(LoginRequiredMixin, ListView):
    model = Order