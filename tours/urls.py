""" URLS for Tours App"""
from django.urls import path
from .views import (
    TourListView,
    TourDetailView,
    BookingView,
    ReviewDeleteView,
    ReviewUpdateView
)

urlpatterns = [
    path('', TourListView.as_view(), name='tours-list'),
    path('tour/<int:pk>/', TourDetailView.as_view(), name='tour-detail'),
    path(
        'bookings/',
        BookingView.as_view(),
        name='bookings'
        ),
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
]
