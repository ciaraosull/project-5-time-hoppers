"""Views for Basket"""
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages


def view_basket(request):
    """ Basket Conents View """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ To Add Quantity of tour tickets & other details to the basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    departure_time = None
    if 'tour_departure_time' in request.POST:
        departure_time = request.POST['tour_departure_time']
    basket = request.session.get('basket', {})

    if departure_time:
        if item_id in list(basket.keys()):
            if departure_time in basket[item_id]['items_by_departure_time'].keys():
                basket[item_id]['items_by_departure_time'][departure_time] += quantity
            else:
                basket[item_id]['items_by_departure_time'][departure_time] = quantity
        else:
            basket[item_id] = {'items_by_departure_time': {departure_time: quantity}}

    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
        else:
            basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """Edit the items in basket"""

    quantity = int(request.POST.get('quantity'))
    departure_time = None
    if 'tour_departure_time' in request.POST:
        departure_time = request.POST['tour_departure_time']
    basket = request.session.get('basket', {})

    if departure_time:
        if quantity > 0:
            basket[item_id]['items_by_departure_time'][departure_time] = quantity
        else:
            del basket[item_id]['items_by_departure_time'][departure_time]
            if not basket[item_id]['items_by_departure_time']:
                basket.pop(item_id)
    else:
        if quantity > 0:
            basket[item_id] = quantity
        else:
            basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('view-basket'))


def remove_from_basket(request, item_id):
    """Remove the item from the basket"""
    redirect_url = request.POST.get('redirect_url')

    try:
        departure_time = None
        if 'tour_departure_time' in request.POST:
            departure_time = request.POST['tour_departure_time']
        basket = request.session.get('basket', {})

        if basket:
            del basket[item_id]['items_by_departure_time'][departure_time]
            if not basket[item_id]['items_by_departure_time']:
                basket.pop(item_id)
        else:
            basket.pop(item_id)

        request.session['basket'] = basket
        return redirect(redirect_url)
        # return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)

# def remove_from_basket(request, item_id):
#     """Remove the item from the basket"""

#     # redirect_url = request.POST.get('redirect_url')

#     # get basket instance or create basket if it doesn't exist
#     basket = request.session.get('basket', {})

#     # if tour is in basket
#     if item_id in list(basket.keys()):
#         # remove from basket
#         basket.pop(item_id)
#         messages.success(request, "Booking has been removed basket.")
#     else:
#         # if tour is not in the basket
#         messages.error(request, "This Booking is not in your basket.")

#     # update the basket
#     request.session['basket'] = basket
#     return redirect('view-basket')
