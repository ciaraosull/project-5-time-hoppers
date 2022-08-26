""" Imports for admin site"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Tour, Category, Review, DepartureTime, Booking


@admin.register(Tour)
class TourAdmin(SummernoteModelAdmin):
    """ Display Tour Model on Admin Site """
    list_display = (
        'date_added',
        'tour_name',
        'category',
        'tour_duration'
        'rating',
        'price',
        'image'
    )
    search_fields = ['tour_name', 'description']
    list_filter = ('date_added', 'price', 'rating')
    summernote_fields = ('description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Display Category Model on Admin Site """
    list_display = ('name', 'friendly_name')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Class to display reviews on admin site"""
    list_display = ('name', 'your_review', 'tour', 'date_posted')
    list_filter = ('date_posted', 'name')
    search_fields = ('name', 'your_review')


@admin.register(DepartureTime)
class DepartureTimeAdmin(admin.ModelAdmin):
    """Class to display reviews on admin site"""
    list_display = ('departure_time')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """ Display Booking Model on Admin Site """
    list_display = (
        'tour_name',
        'book_tour_date',
        'departure_time',
        'quantity'
        'date_added'
    )
    search_fields = ['tour_name']
    list_filter = ('date_added', 'quantity', 'book_tour_date')
