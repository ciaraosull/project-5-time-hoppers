""" Imports for admin site"""
from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """ Display Booking Model on Admin Site """
    list_display = (
        'tour_name',
        'book_tour_date',
        'departure_time',
        'quantity',
        'date_added'
    )
    search_fields = ['tour_name']
    list_filter = ('date_added', 'quantity', 'book_tour_date')
