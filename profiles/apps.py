"""Imports for configuring attributes of app"""
from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """Instance of the app class with attributed set"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'

    def ready(self):
        """Import the Profile Signals"""
        import profiles.signals
