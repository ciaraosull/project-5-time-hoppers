"""Imports for Profile Model"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    """ Model for Profile """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = CloudinaryField('image', blank=True)

    def __str__(self):
        """ To return the user's username object as a string """
        return f'Profile for {self.user.username}'
