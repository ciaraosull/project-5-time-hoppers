""" Context Processor"""
from django.shortcuts import get_object_or_404
from tours.models import Tour


def basket_contents(request):
    """To make all available in every template across all apps"""

    basket_items = []
    total = 0
    tour_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        tour = get_object_or_404(Tour, pk=item_id)
        total += quantity * tour.price
        tour_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'tour': tour,
        })

    context = {
        'basket_items': basket_items,
        'total': total,
        'tour_count': tour_count,
    }

    return context
