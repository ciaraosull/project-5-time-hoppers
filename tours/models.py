""" Imports for Tours """
from django.db import models


class Category(models.Model):
    """ Categorise for User to Filter Tours"""
    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        """ To return the name objects as a string """
        return self.name

    def get_friendly_name(self):
        """ To return the friendly name objects as a string """
        return self.friendly_name


class Tour(models.Model):
    """ Tour Details"""
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    tour_name = models.CharField(max_length=254)
    description = models.TextField()
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    tour_date = models.DateField()

    def __str__(self):
        """ To return the name objects as a string """
        return self.tour_name
