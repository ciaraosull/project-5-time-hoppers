"""Register Profile with admin site"""
from django.contrib import admin
from .models import Profile


admin.site.register(Profile)
