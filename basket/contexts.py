"""Context Processor"""
from django.shortcuts import get_object_or_404
from tours.models import Tour


def basket_contents(request):
    """To make all available in every template across all apps"""

    basket_items = []
    total = 0
    tour_count = 0
    basket = request.session.get('basket', {})

    for item_id, item_data in basket.items():
        tour = get_object_or_404(Tour, pk=item_id)
        tour += item_data * tour.price
        tour_count += item_data
        basket_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'tour': tour,
        })

    context = {
        'basket_items': basket_items,
        'total': total,
        'tour_count': tour_count
    }

    return context
