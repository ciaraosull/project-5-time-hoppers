""" URLS for Tours App"""
from django.urls import path
from .views import AboutUsListView

urlpatterns = [
    path('', AboutUsListView.as_view(), name='about-us'),
]
