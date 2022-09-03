"""Views for Basket"""
from django.shortcuts import render, redirect


def view_basket(request):
    """ Basket Conents View """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ To Add Quantity of tour tickets & other details to the basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    departure_times = None
    if 'departure_times' in request.POST:
        departure_times = request.POST['tour_departure_times']
    basket = request.session.get('basket', {})

    if departure_times:
        if item_id in list(basket.keys()):
            if departure_times in basket[item_id]['items_by_departure_times'].keys():
                basket[item_id]['items_by_departure_times'][departure_times] += quantity
            else:
                basket[item_id]['items_by_departure_times'][departure_times] = quantity
        else:
            basket[item_id] = {'items_by_departure_times': {departure_times: quantity}}
    else:

        if item_id in list(basket.keys()):
            basket[item_id] += quantity
        else:
            basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)
