"""Views for Basket"""
from django.shortcuts import render, redirect


def view_basket(request):
    """ Basket Conents View """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ To Add Quantity of tour tickets & other details to the basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
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
