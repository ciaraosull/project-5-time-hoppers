"""
Imports for Shopping Basket View
"""
from django.shortcuts import render, redirect


def view_basket(request):
    """ A view that renders the bag contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, fields_id):
    """ View to add booking to basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # save basket bookings during session so items not lost
    basket = request.session.get('basket', {})

    if fields_id in list(basket.keys()):
        basket[fields_id] += quantity
    else:
        basket[fields_id] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)
