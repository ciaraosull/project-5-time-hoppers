"""Imports for configuring attributes of Home App"""
from django.apps import AppConfig


class HomeConfig(AppConfig):
    """Home App Config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
