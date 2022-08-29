""" URLS for Basket App"""
from django.urls import path
from .views import (
    BasketListView,
    BookingView,
)


urlpatterns = [
    path('', BasketListView.as_view(), name='view-basket'),
    path(
        '<int:pk>/bookings/',
        BookingView.as_view(),
        name='bookings'
        ),
]
