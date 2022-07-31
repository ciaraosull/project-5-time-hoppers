""" Imports for admin site"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Tour, Category


@admin.register(Tour)
class PostAdmin(SummernoteModelAdmin):
    """ Display Tour Model on Admin Site """
    list_display = ('tour_name', 'category')
    search_fields = ['tour_name', 'description']
    list_filter = ('price', 'rating')
    summernote_fields = ('description')


admin.site.register(Category)
