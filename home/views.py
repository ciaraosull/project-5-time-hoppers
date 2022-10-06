"""
Imports for Home Views
"""
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """ Class-based view to return home page """
    template_name = 'home/index.html'


class PrivacyView(TemplateView):
    """ Class-based view to return home page """
    template_name = 'home/privacy_statement.html'


class AccessibilityView(TemplateView):
    """ Class-based view to return home page """
    template_name = 'home/accessibility.html'
