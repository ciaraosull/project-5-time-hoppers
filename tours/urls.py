""" URLS for Tours App"""
from django.urls import path
from .views import TourListView

urlpatterns = [
    path('', TourListView.as_view(), name='tours-list'),
]
