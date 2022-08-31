""" URLS for Basket App"""
from django.urls import path
from .views import (
    BookingListView,
    BookingCreateView,
    BookingUpdateView
)


urlpatterns = [
    path('', BookingListView.as_view(), name='view-basket'),
    path(
        '<int:pk>/bookings/',
        BookingCreateView.as_view(),
        name='bookings'
        ),
    path(
        '<int:pk>/bookings/update/',
        BookingUpdateView.as_view(),
        name='bookings-update'
        ),
]
