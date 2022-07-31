""" URLS for Tours App"""
from django.urls import path
from .views import TourListView, TourDetailView

urlpatterns = [
    path('', TourListView.as_view(), name='tours-list'),
    path('tour/<int:pk>/', TourDetailView.as_view(), name='tour-detail'),
]
