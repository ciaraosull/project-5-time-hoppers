""" Imports for Tours """
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """ Categorise for User to Filter Tours"""
    category_name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)

    class Meta:
        """ To display the plural"""
        verbose_name_plural = 'Categories'

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
        max_digits=5, decimal_places=0, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ To display the tours by date added in desending order """
        ordering = ['-date_added']

    def __str__(self):
        """ To return the name objects as a string """
        return self.tour_name


class Review(models.Model):
    """ Model for Comments """
    tour = models.ForeignKey(
        Tour, on_delete=models.CASCADE, related_name='reviews')
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='commenter')
    your_review = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Ordering reviews by first created """
        ordering = ["date_posted"]

    def __str__(self):
        return f"Review {self.your_review} by {self.name}"
