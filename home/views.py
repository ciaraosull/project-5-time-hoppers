"""
Imports for Home Views
"""
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """ Class-based view to return home page """
    template_name = 'home/index.html'
