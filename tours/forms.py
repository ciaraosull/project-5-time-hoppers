"""Form for Reviews"""
from django import forms
from .models import Review, Tour


class TourForm(forms.ModelForm):
    """Create a form for admin users to add tours"""
    class Meta:
        """
        To state what model to use
        and what fields to display on the form
        """
        model = Tour
        fields = (
            'category',
            'tour_name',
            'description',
            'tour_duration',
            'accessibility_friendly',
            'rating',
            'departure_time',
            'has_departure_date',
            'price',
            'image_url',
            'image',
        )


class ReviewForm(forms.ModelForm):
    """Create a form for users to leave reviews on tour page"""
    class Meta:
        """
        To state what model to use
        and what fields to display on the form
        """
        model = Review
        fields = ('your_review',)
