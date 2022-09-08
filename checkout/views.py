"""Views for Checkout Page"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """To create a view for the checkout &
    redirect users if checkout typed into url
    """
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your Basket is Empty")
        return redirect(reverse('tours-list'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
