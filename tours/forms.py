"""Form for Reviews"""
from django import forms
from .models import Booking, Review


class DateInput(forms.DateInput):
    """Change input type to date picker"""
    input_type = 'date'


class BookingForm(forms.ModelForm):
    """ Create a Booking """
    class Meta:
        """
        Get booking model and choose fields to display
        """
        DEPARTURE_TIME_CHOICES = [
            ('9:00', '9am'),
            ('11:00', '11am'),
            ('13:00', '1pm'),
            ('15:00', '3pm'),
            ('20:00', '8pm'),
            ]
        model = Booking
        departure_time = forms.ChoiceField(
            choices=DEPARTURE_TIME_CHOICES,
            required=True
            )

        fields = [
            'book_tour_date',
            'departure_time',
            'quantity',
            'notes'
            ]

        widgets = {
            'book_tour_date': DateInput()
            }


class ReviewForm(forms.ModelForm):
    """Create a form for users to leave reviews on tour page"""
    class Meta:
        """
        To state what model to use
        and what fields to display on the form
        """
        model = Review
        fields = ('your_review',)
