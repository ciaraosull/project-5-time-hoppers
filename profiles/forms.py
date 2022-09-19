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
        fields = ('profile_image', 'default_phone_number',
                  'default_street_address1', 'default_street_address2',
                  'default_town_or_city', 'default_county', 'default_postcode',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County or State',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'profile_image':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black'
            self.fields[field].label = False
