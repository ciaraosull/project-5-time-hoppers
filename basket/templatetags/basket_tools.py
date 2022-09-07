"""To Calculate the final total"""
from django import template
from django.utils import timezone as tz


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    """To return the final total of price by quantity"""
    return price * quantity
