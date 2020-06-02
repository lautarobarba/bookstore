from django.apps import AppConfig


class ShoppingcartConfig(AppConfig):
    name = 'shoppingcart'

    def ready(self):
        import shoppingcart.signals