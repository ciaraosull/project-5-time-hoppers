"""
Imports for Shopping Basket View
"""
from django.views.generic import TemplateView


class BasketView(TemplateView):
    """ Class-based view to return shopping basket page """
    template_name = 'basket/basket.html'
