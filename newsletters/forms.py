"""Forms for Newsletters & Subscribers"""
from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Subscriber, Newsletter


class SubsciberForm(forms.ModelForm):
    """ Create a Subscribers Form """
    class Meta:
        """
        To state what model to use
        and what fields to display on the form
        """
        model = Subscriber
        fields = ['email', ]


class NewsletterForm(forms.ModelForm):
    """ Create a Newsletter Form """
    class Meta:
        """
        Get newsletter model, choose fields to display
        and add summernote widget
        """
        model = Newsletter
        fields = [
            'title',
            'message',
            ]

        widgets = {
            'message': SummernoteWidget(),
            }
