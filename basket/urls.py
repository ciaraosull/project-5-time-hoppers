""" URLS for Basket App"""
from django.urls import path
from .views import (
    BookingListView,
    BookingCreateView,
    # add_to_basket,
    BookingUpdateView,
    BookingDeleteView
)

# from . import views


urlpatterns = [
    path('', BookingListView.as_view(), name='view-basket'),
    path(
        '<int:pk>/bookings/',
        BookingCreateView.as_view(),
        name='bookings'
        ),
    # path(
    #     'add-to-basket/<int:pk>', add_to_basket,
    #     name='add-to-basket'
    #     ),

    # path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path(
        '<int:pk>/bookings/update/',
        BookingUpdateView.as_view(),
        name='bookings-update'
        ),
    path(
        '<int:pk>/bookings/delete/',
        BookingDeleteView.as_view(),
        name='bookings-delete'
        ),
]
