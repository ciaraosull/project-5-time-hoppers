"""
Imports for Tours View
"""
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from .models import Tour, Review
from .forms import ReviewForm


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

    def tour(self, request, pk):
        """
        To get the tour detail view and display comment form
        if user is logged in.  If form is valid then,
        save the details of the comment form and include username
        """
        tour = get_object_or_404(Tour, pk=pk)
        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review_form.instance.name = request.user
            review_form.instance.tour = tour
            review = review_form.save(commit=False)
            review.name = request.user
            review.tour = tour
            review.save()
            messages.success(request, 'Your Review Was Successfully Added')
            return redirect('tour-detail', tour.pk)
        else:
            review_form = ReviewForm()

    def get_context_data(self, **kwargs):
        """
        To display the review form and
        paginate reviews list if the user is logged in
        """
        context = super().get_context_data()
        pk = self.kwargs['pk']
        tour = get_object_or_404(Tour, pk=pk)
        reviews = Review.objects.filter(tour=tour)
        paginator = Paginator(reviews, 6)
        page = self.request.GET.get('page')
        context['reviewa'] = paginator.get_page(page)
        context['page'] = page
        context['paginator'] = paginator
        context['review_form'] = ReviewForm()
        return context
