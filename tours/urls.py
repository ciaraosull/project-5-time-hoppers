""" URLS for Tours App"""
from django.urls import path
from .views import (
    TourListView,
    TourDetailView,
    TourCreateView,
    ReviewDeleteView,
    ReviewUpdateView
)

from . import views

urlpatterns = [
    path('', TourListView.as_view(), name='tours-list'),
    path('<int:pk>/', TourDetailView.as_view(), name='tour-detail'),
    path('new/', TourCreateView.as_view(), name='tour-form'),
    path(
        'reviews/<int:pk>/update/',
        ReviewUpdateView.as_view(),
        name='review-update'
        ),
    path(
        'reviews/<int:pk>/delete/',
        ReviewDeleteView.as_view(),
        name='review-delete'
        ),
    path('<tour_id>', views.tour_booking_detail, name='tour_booking_detail'),
]
