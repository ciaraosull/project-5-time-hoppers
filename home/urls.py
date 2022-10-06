""" URLS for Home App"""
from django.urls import path
from home.views import HomeView, PrivacyView, AccessibilityView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('privacy/', PrivacyView.as_view(), name='privacy'),
    path('accessibility/', AccessibilityView.as_view(), name='accessibility'),
]
