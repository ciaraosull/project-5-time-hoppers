"""Newsletter Models"""
from django.db import models


class Subscriber(models.Model):
    """Model for Subscribers emails"""
    email = models.EmailField(null=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    """Model for Newletters"""
    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)
    date_posted = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
