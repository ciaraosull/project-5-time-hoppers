"""
Imports for Shopping Basket View
"""
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    View
)
from django.urls import reverse_lazy
from django.utils import timezone
from tours.models import Tour
from .models import Booking, BookingItem, Basket
from .forms import BookingForm


class BookingCreateView(LoginRequiredMixin, CreateView):
    """ Booking """
    Model = Booking
    form_class = BookingForm
    context_object_name = 'bookings'
    template_name = 'basket/booking_form.html'
    success_url = reverse_lazy('tours-list')

    def form_valid(self, form):
        """ Save booking for chosen tour name & show success message """
        pk = self.kwargs['pk']
        tour = get_object_or_404(Tour, pk=pk)
        booking_form = BookingForm(data=self.request.POST)

        if booking_form.is_valid():
            booking_form.instance.user = self.request.user
            booking_form.instance.tour = tour
            booking_form.user = self.request.user
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


class BookingListView(LoginRequiredMixin, ListView):
    """Class to show the posts in list view on home page """
    model = Booking
    template_name = 'basket/basket.html'
    context_object_name = 'bookings'
    ordering = ['-date_added']

    def get_queryset(self):
        """Only show Bookings by User """
        # return Booking.objects.aggregate(Sum('total_price'))['grand_total__sum']
        return Booking.objects.filter(user=self.request.user)


class BookingUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SuccessMessageMixin,
    UpdateView
):
    """ Class to allow logged in users to update bookings """
    model = Booking
    form_class = BookingForm
    context_object_name = 'bookings'
    success_url = reverse_lazy('view-basket')
    success_message = 'Booking Successfully Updated'

    def form_valid(self, form):
        """Function to set signed in user as author of updated booking"""
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        To set test_func to ensure only the user of the booking can update it
        and show 403 forbidden if url entered by another user
        """
        return self.request.user == self.get_object().user


class BookingDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SuccessMessageMixin,
    DeleteView
):
    """
    Allow user who created booking to delete it.
    """
    model = Booking
    context_object_name = 'bookings'
    success_url = reverse_lazy('view-basket')
    success_message = 'Booking Successfully Deleted'

    def test_func(self):
        """
        To set test_func to ensure only the author of the booking can delete it
        and show 403 forbidden if url entered by another user
        """
        return self.request.user == self.get_object().user


def add_to_basket(request, pk):
    """Take the booking, create a booking item and assign to the basket"""
    booking = get_object_or_404(Booking, pk=pk)
    print('test1')
    booking_item, created = BookingItem.objects.get_or_create(
        booking=booking,
        user=request.user,
        booked=False
    )
    basket_qs = Basket.objects.filter(user=request.user, booked=False)
    if basket_qs. exists():
        basket = basket_qs[0]
        print('test2')
        if basket.booking_items.filter(booking__pk=booking.pk).exists():
            booking_item.quantity += 1
            booking_item.save()
            print('test3')
        else:
            basket.booking_items.add(booking_item)
            print('test4')
    else:
        date_added = timezone.now()
        basket = Basket.objects.create(
            user=request.user, date_added=date_added)
        basket.booking_items.add()
        print('test 5')
    return redirect('order')


class OrderDetailView(View):
    """
    To show the order containing all
    the bookings made by the user before payment
    """
    template_name = "order.html"



# def add_to_bag(request, item_id):
#     """ Add a quantity of the specified product to the shopping bag """

#     booking = get_object_or_404(Booking, pk=item_id)
#     quantity = int(request.POST.get('quantity'))
#     redirect_url = request.POST.get('redirect_url')
#     size = None
#     if 'product_size' in request.POST:
#         size = request.POST['product_size']
#     bag = request.session.get('bag', {})

#     if size:
#         if item_id in list(bag.keys()):
#             if size in bag[item_id]['items_by_size'].keys():
#                 bag[item_id]['items_by_size'][size] += quantity
#                 messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
#             else:
#                 bag[item_id]['items_by_size'][size] = quantity
#                 messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
#         else:
#             bag[item_id] = {'items_by_size': {size: quantity}}
#             messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
#     else:
#         if item_id in list(bag.keys()):
#             bag[item_id] += quantity
#             messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
#         else:
#             bag[item_id] = quantity
#             messages.success(request, f'Added {product.name} to your bag')

#     request.session['bag'] = bag
#     return redirect(redirect_url)