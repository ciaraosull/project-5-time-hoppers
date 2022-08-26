"""Form for Reviews"""
from django import forms
from .models import Review


class DateInput(forms.DateInput):
    """Change input type to date picker"""
    input_type = 'date'


class ReviewForm(forms.ModelForm):
    """Create a form for users to leave reviews on tour page"""
    class Meta:
        """
        To state what model to use
        and what fields to display on the form
        """
        model = Review
        fields = ('your_review',)
