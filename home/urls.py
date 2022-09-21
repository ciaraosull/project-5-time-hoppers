""" URLS for Home App"""
from django.urls import path
from home.views import HomeView
from . import views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('subscribe/', views.subscribe, name='subscribe'),
]
