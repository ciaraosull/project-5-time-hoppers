""" Imports for admin site"""
from django.contrib import admin
from .models import Booking, Basket


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """ Display Booking Model on Admin Site """
    list_display = (
        'tour',
        'book_tour_date',
        'departure_time',
        'quantity',
        'date_added',
        'booked',
        'notes'
    )
    search_fields = ['tour']
    list_filter = ('date_added', 'booked', 'book_tour_date')


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    """ Display Basket Model on Admin Site """
    list_display = (
        'user',
        'date_added',
        'booked',
    )
    search_fields = ['booked']
    list_filter = ('date_added', 'booked')
