""" Imports for Tours """
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """ Categorise for User to Filter Tours"""
    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)

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
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    tour_name = models.CharField(max_length=250)
    description = models.TextField()
    tour_duration = models.CharField(
        null=True,
        max_length=250,
        help_text="Specify quantity by days or hours only"
        )
    accessibility_friendly = models.BooleanField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=5, decimal_places=0, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ To display the tours by date added in desending order """
        ordering = ['-date_added']

    def __str__(self):
        """ To return the name objects as a string """
        return f"Tour Name: {self.tour_name}"


class Review(models.Model):
    """ Model for User Reviews """
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


class Booking(models.Model):
    """ Model for Booking """
    DEPARTURE_TIME_CHOICES = [
        ('9:00', '9am'),
        ('11:00', '11am'),
        ('13:00', '1pm'),
        ('15:00', '3pm'),
        ('20:00', '8pm'),
        ]

    tour_name = models.ForeignKey(
        Tour, on_delete=models.CASCADE, related_name='bookings')
    book_tour_date = models.DateField()
    departure_time = models.CharField(
        max_length=5,
        choices=DEPARTURE_TIME_CHOICES
        )
    quantity = models.PositiveSmallIntegerField(
        help_text="Number of TimeHoppers over 18 years old only"
        )
    notes = models.TextField(
        null=True,
        max_length=500,
        help_text="Note Any Specific Requirements Here"
        )
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ To display the booking by created on in desending order """
        ordering = ['-book_tour_date']

    def __str__(self):
        """ To return the individual title objects as a string """
        return f"Booking: {self.tour_name} on {self.book_tour_date}"
