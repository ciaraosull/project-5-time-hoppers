"""Register Newsletter & Subscribers to Admin Site"""
from django.contrib import admin
from .models import Newsletter, Subscriber


@admin.register(Subscriber)
class CommentAdmin(admin.ModelAdmin):
    """Class to display Subscribers on admin site"""
    list_display = ('email', 'date_subscribed')
    list_filter = ('date_subscribed', 'email')


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    """ Class admin site newsletter """
    list_display = ('title', 'date_posted')
    list_filter = ('date_posted', 'title')
