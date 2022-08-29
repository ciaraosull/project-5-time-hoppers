""" Imports for Bookings """
from django.db import models
from tours.models import Tour


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
        help_text="Note Any Specific Requirements Here",
        blank=True
        )
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ To display the booking by created on in desending order """
        ordering = ['-book_tour_date']

    def __str__(self):
        """ To return the individual title objects as a string """
        return f"Booking: {self.tour_name} on {self.book_tour_date}"
