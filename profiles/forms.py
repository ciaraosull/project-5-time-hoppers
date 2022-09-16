"""Imports for User Profile Form"""
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserUpdateForm(forms.ModelForm):
    """Create User Profile Update form"""
    email = forms.EmailField()

    class Meta:
        """Get the user model & choose fields to update"""
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """ Create a Profile Form"""
    class Meta:
        """
        Get profile model and choose fields to display
        """
        model = Profile
        fields = ['profile_image']
