""" URLS for Basket App"""
from django.urls import path
from .views import (
    BookingListView,
    BookingView,
    BookingUpdateView
)


urlpatterns = [
    path('', BookingListView.as_view(), name='view-basket'),
    path(
        '<int:pk>/bookings/',
        BookingView.as_view(),
        name='bookings'
        ),
    path(
        '<int:pk>/bookings/update/',
        BookingUpdateView.as_view(),
        name='booking-update'
        ),
]
