""" Imports for admin site"""
from django.contrib import admin
from .models import StaffMember


@admin.register(StaffMember)
class CategoryAdmin(admin.ModelAdmin):
    """ Display Staff Member Model on Admin Site """
    list_display = (
        'full_name',
        'tour',
        'multi_lingual',
        'date_started',
        'faviourite_era',
    )
    search_fields = ['full_name', 'tour']
    list_filter = ('date_added', 'tour')
