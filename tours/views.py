"""
Imports for Tours View
"""
from django.views.generic import ListView, DetailView
from .models import Tour


class TourListView(ListView):
    """ A view to show all tours including sort & search """
    model = Tour
    template_name = 'tours/tours.html'
    context_object_name = 'tours'
    ordering = ['-date_added']
    paginate_by = 6


class TourDetailView(DetailView):
    """ Class to show the individual tours in a detail view """
    model = Tour
