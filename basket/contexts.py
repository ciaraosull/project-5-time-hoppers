""" Context Processor"""
from django.shortcuts import get_object_or_404
from tours.models import Tour


def basket_contents(request):
    """To make all available in every template across all apps"""

    basket_items = []
    total = 0
    tour_count = 0
    basket = request.session.get('basket', {})

    for item_id, item_data in basket.items():
        if isinstance(item_data, int):
            tour = get_object_or_404(Tour, pk=item_id)
            total += item_data * tour.price
            tour_count += item_data
            basket_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'tour': tour,
            })

        else:
            tour = get_object_or_404(Tour, pk=item_id)
            for departure_time, quantity in item_data['items_by_departure_time'].items():
                total += quantity * tour.price
                tour_count += quantity
                basket_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'tour': tour,
                    'departure_time': departure_time,
                })

    context = {
        'basket_items': basket_items,
        'total': total,
        'tour_count': tour_count,
    }

    return context
