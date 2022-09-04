"""Views for Basket"""
from django.shortcuts import render, redirect, reverse, HttpResponse


def view_basket(request):
    """ Basket Conents View """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ To Add Quantity of tour tickets & other details to the basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # departure_date = None
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

    # if 'tour_departure_date' in request.POST:
    #     departure_date = request.POST['tour_departure_date']
    # basket = request.session.get('basket', {})

    # if departure_date:
    #     if item_id in list(basket.keys()):
    #         if departure_date in basket[item_id]['items_by_departure_date'].keys():
    #             basket[item_id]['items_by_departure_date'][departure_date] += quantity
    #         else:
    #             basket[item_id]['items_by_departure_date'][departure_date] = quantity
    #     else:
    #         basket[item_id] = {'items_by_departure_date': {departure_date: quantity}}
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
