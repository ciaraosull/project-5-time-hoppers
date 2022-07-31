""" Imports for admin site"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Tour, Category


@admin.register(Tour)
class TourAdmin(SummernoteModelAdmin):
    """ Display Tour Model on Admin Site """
    list_display = ('date_added', 'tour_name', 'category', 'rating', 'price', 'image')
    search_fields = ['tour_name', 'description']
    list_filter = ('date_added', 'price', 'rating')
    summernote_fields = ('description')


@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):
    """ Display Category Model on Admin Site """
    list_display = ('category_name', 'friendly_name')
