""" Imports for staff model """
from django.db import models
from cloudinary.models import CloudinaryField
from tours.models import Tour


class StaffMember(models.Model):
    """ Model for Staff Members """
    full_name = models.CharField(max_length=200, unique=True)
    profile_image = CloudinaryField('image', blank=True)
    tour = models.ForeignKey(
        Tour,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Specify tour this staff member is currently working on"
        )
    multi_lingual = models.BooleanField(
        null=True,
        blank=True
        )
    date_started = models.DateField()
    faviourite_era = models.TextField()
    social_media_link = models.URLField(max_length=200, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ To display the staff by created on in desending order """
        ordering = ['-date_added']

    def __str__(self):
        """ To return the individual title objects as a string """
        return f"{self.full_name}"
