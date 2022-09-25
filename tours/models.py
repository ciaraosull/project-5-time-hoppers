""" Imports for Tours """
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """ Categorise for User to Filter Tours"""
    name = models.CharField(max_length=250)
    friendly_name = models.CharField(
        max_length=250,
        null=True,
        blank=True
        )

    class Meta:
        """ To display the plural"""
        verbose_name_plural = 'Categories'

    def __str__(self):
        """ To return the name objects as a string """
        return f"Category Name: {self.name}"

    def get_friendly_name(self):
        """ To return the friendly name objects as a string """
        return self.friendly_name


class Tour(models.Model):
    """ Tour Details"""
    DEPARTURE_TIME_CHOICES = [
        ('9am', '9am'),
        ('11am', '11am'),
        ('1pm', '1pm'),
        ('3pm', '3pm'),
        ('8pm', '8pm'),
        ]

    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
        )
    tour_name = models.CharField(max_length=250)
    description = models.TextField()
    tour_duration = models.CharField(
        null=True,
        max_length=250,
        help_text="Specify quantity by days or hours only"
        )
    accessibility_friendly = models.BooleanField(
        null=True,
        blank=True
        )
    rating = models.DecimalField(
        max_digits=5,
        decimal_places=0,
        null=True,
        blank=True
        )
    departure_time = models.CharField(
        blank=True,
        max_length=5,
        choices=DEPARTURE_TIME_CHOICES
        )
    has_departure_date = models.BooleanField(
        default=True,
        blank=True,
        null=True,
        )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=0
        )
    image_url = models.URLField(
        null=True,
        blank=True
        )
    image = CloudinaryField('image', null=True, blank=True)

    date_added = models.DateTimeField(
        auto_now_add=True
        )

    class Meta:
        """ To display the tours by date added in desending order """
        ordering = ['-date_added']

    def __str__(self):
        """ To return the name objects as a string """
        return f"{self.tour_name}"


class Review(models.Model):
    """ Model for User Reviews """
    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name='reviews'
        )
    name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='commenter'
        )
    your_review = models.TextField()
    date_posted = models.DateTimeField(
        auto_now_add=True
        )

    class Meta:
        """ Ordering reviews by first created """
        ordering = ["date_posted"]

    def __str__(self):
        return f"Review {self.your_review} by {self.name}"
