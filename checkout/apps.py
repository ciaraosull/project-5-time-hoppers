"""Imports for configuring attributes of Basket App"""
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """ Checkout App Config """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        """ Import Checkout Signal """
        import checkout.signals
