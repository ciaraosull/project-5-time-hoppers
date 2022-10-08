"""Imports for configuring attributes of Newletters App"""
from django.apps import AppConfig


class NewslettersConfig(AppConfig):
    """Newsletter App Config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newsletters'
