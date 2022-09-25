"""Imports for Profile Model"""
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    """ Model for Profile """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = CloudinaryField('image', blank=True)

    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)

    default_country = CountryField(
        blank_label='Country *', null=True, blank=True)

    default_postcode = models.CharField(
        max_length=20, null=True, blank=True)

    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)

    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)

    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)

    default_county = models.CharField(
        max_length=80, null=True, blank=True)

    def __str__(self):
        """ To return the user's username object as a string """
        return f'Profile for {self.user.username}'
