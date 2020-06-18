from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from market.models import Discount
from django.urls import reverse_lazy

class DiscountCreateView(LoginRequiredMixin, CreateView):
    model = Discount
    template_name = 'market/discount_create.html'
    fields = '__all__'

class DiscountListView(LoginRequiredMixin, ListView):
    model = Discount
    queryset = Discount.objects.order_by('name')
    paginate_by = 10

class DiscountUpdateView(LoginRequiredMixin, UpdateView):
    model = Discount
    template_name = 'market/discount_update.html'
    fields = '__all__'

class DiscountDeleteView(LoginRequiredMixin, DeleteView):
    model = Discount
    template_name = 'market/discount_delete.html'
    success_url = reverse_lazy('discount-list')