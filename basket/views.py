"""
Imports for Shopping Basket View
"""
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import (
    ListView,
    FormView,
)
from django.urls import reverse_lazy
from tours.models import Tour
from .models import Booking, Basket
from .forms import BookingForm


class BookingView(LoginRequiredMixin, FormView):
    """ Booking """
    Model = Booking
    form_class = BookingForm
    context_object_name = 'booking'
    template_name = 'basket/booking_form.html'
    success_url = reverse_lazy('view-basket')

    def form_valid(self, form):
        """ Save booking for chosen tour name & show success message """
        pk = self.kwargs['pk']
        tour = get_object_or_404(Tour, pk=pk)
        booking_form = BookingForm(data=self.request.POST)

        if booking_form.is_valid():
            booking_form.instance.name = self.request.user
            booking_form.instance.tour = tour
            booking_form.name = self.request.user
            booking = booking_form.save(commit=False)
            booking_form.tour = tour
            booking.save()
            messages.success(self.request, 'Booking Successfully Added')
            return redirect('view-basket')
        booking_form = BookingForm()

    def get_context_data(self, **kwargs):
        """
        Define context data to display chosen tour name in booking form
        """
        context = super().get_context_data()
        pk = self.kwargs['pk']
        tour = get_object_or_404(Tour, pk=pk)
        booking = Booking.objects.filter(tour=tour)
        booking.tour_name = tour
        context['tour_name'] = tour
        return context


class BasketListView(LoginRequiredMixin, ListView):
    """Class to show the posts in list view on home page """
    model = Booking
    template_name = 'basket/basket.html'
    context_object_name = 'bookings'
    ordering = ['-date_added']

    def get_queryset(self):
        """Only show Bookings by User """
        return Booking.objects.filter(name=self.request.user)



