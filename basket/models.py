""" Imports for Bookings """
from django.contrib.auth.models import User
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

    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='user'
        )
    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name='bookings',
        )
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
        ordering = ['-date_added']

    def total_price(self):
        """ To get the total price of each booking """
        total = self.quantity * self.tour.price
        return total

    def __str__(self):
        """ To return the individual title objects as a string """
        return f"Booking: {self.tour.tour_name}"


class BookingItem(models.Model):
    """ Model for Booking """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        )

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    booked = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ To return the individual title objects as a string """
        return f"{self.quantity} for {self.booking.tour.tour_name}"


class Basket(models.Model):
    """ Model for Basket to contain Booking Items """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
        )
    booking_items = models.ManyToManyField(
        Booking, related_name='booking_items')
    date_added = models.DateTimeField(auto_now_add=True)
    booked = models.BooleanField(default=False)

    class Meta:
        """ To display the basket by created on in desending order """
        ordering = ['-date_added']

    def __str__(self):
        """ To return the individual title objects as a string """
        return f"Basket: {self.booking_items} added on {self.date_added}"

    # def grand_total(self):
    #     total = 0
    #     for booking_items in self.tour.all():
    #         total += booking_items.get_total_price()
    #     return total
