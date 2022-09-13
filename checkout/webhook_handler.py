"""Handle Stripe Webhooks"""
from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        """Assign request as attribute of the class
        for access attributes from Stripe
        """
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        and return response indicating recieved
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
