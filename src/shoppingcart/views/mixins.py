from django.views import View
from django.views.generic.base import ContextMixin

class CartOwnerMixin(ContextMixin, View):
    """
    Allow owners to edit only their profiles
    """
    def get(self, request, *args, **kwargs):
        # Check if user is anonymous
        # anonymous.id is always None
        if request.user.id:
            # User can edit only his own cart
            logged_user_cart = request.user.cart.pk
            current_cart = self.kwargs['pk']
            self.can_edit = logged_user_cart == current_cart
        else:
            self.can_edit = False
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['can_edit'] = self.can_edit
        return context