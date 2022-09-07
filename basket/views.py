"""Views for Basket"""
from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponse
)
from django.contrib import messages
from tours.models import Tour


def view_basket(request):
    """ Basket Conents View """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ To Add Quantity of tour tickets & other details to the basket """

    tour = get_object_or_404(Tour, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    departure_date = None

    if 'tour_departure_date' in request.POST:

        departure_date = request.POST['tour_departure_date']
    basket = request.session.get('basket', {})

    if departure_date:
        if item_id in list(basket.keys()):
            if departure_date in basket[item_id]['items_by_departure_date'].keys():
                basket[item_id]['items_by_departure_date'][departure_date] += quantity
            else:
                basket[item_id]['items_by_departure_date'][departure_date] = quantity
        else:
            basket[item_id] = {'items_by_departure_date': {departure_date: quantity}}

    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
        else:
            basket[item_id] = quantity

    request.session['basket'] = basket
    messages.success(request, f'{tour.tour_name} on {departure_date} Added to your Basket')
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """Edit the items in basket"""

    tour = get_object_or_404(Tour, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    departure_date = None
    if 'tour_departure_date' in request.POST:
        departure_date = request.POST['tour_departure_date']
    basket = request.session.get('basket', {})

    if departure_date:
        if quantity > 0:
            basket[item_id]['items_by_departure_date'][departure_date] = quantity
        else:
            del basket[item_id]['items_by_departure_date'][departure_date]
            if not basket[item_id]['items_by_departure_date']:
                basket.pop(item_id)
    else:
        if quantity > 0:
            basket[item_id] = quantity
        else:
            basket.pop(item_id)

    request.session['basket'] = basket
    messages.success(request, f'{tour.tour_name} on {departure_date} Updated')
    return redirect(reverse('view-basket'))


def remove_from_basket(request, item_id):
    """Remove the item from the basket"""

    try:
        tour = get_object_or_404(Tour, pk=item_id)
        departure_date = None
        if 'tour_departure_date' in request.POST:
            departure_date = request.POST['tour_departure_date']
        basket = request.session.get('basket', {})

        if departure_date:
            del basket[item_id]['items_by_departure_date'][departure_date]
            if not basket[item_id]['items_by_departure_date']:
                basket.pop(item_id)
            messages.success(request, f'Removed {tour.tour_name} on {departure_date} from your basket')
        else:
            basket.pop(item_id)
            messages.success(request, f'Removed {tour.tour_name} tours from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
