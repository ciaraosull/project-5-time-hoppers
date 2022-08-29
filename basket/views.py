"""
Imports for Shopping Basket View
"""
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import (
    ListView,
    FormView,
)
from django.urls import reverse_lazy
from tours.models import Tour
from .models import Booking
from .forms import BookingForm


class BookingView(FormView):
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
            booking_form.instance.tour_name = tour
            booking = booking_form.save(commit=False)
            booking.tour_name = tour
            booking.save()
            messages.success(self.request, 'Booking Was Successfully Added')
            return redirect('view-basket')
        booking_form = BookingForm()

    def get_context_data(self, **kwargs):
        """
        Define context data to display chosen tour name in booking form
        """
        context = super().get_context_data()
        pk = self.kwargs['pk']
        tour = get_object_or_404(Tour, pk=pk)
        booking = Booking.objects.filter(tour_name=tour)
        booking.tour_name = tour
        context['tour_name'] = tour
        return context


class BasketListView(ListView):
    """Class to show the posts in list view on home page """
    model = Booking
    template_name = 'basket/basket.html'
    context_object_name = 'bookings'
    ordering = ['-date_added']
    paginate_by = 6
