"""
Imports for Tours View
"""
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
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

    def get_queryset(self):
        """
        Define query_set to get user search results, search by category or sort
        """
        queryset = super().get_queryset()
        if self.request.GET:

            # sort by
            if 'sort' in self.request.GET:
                sort = self.request.GET['sort']
                if sort == 'tour_name':
                    queryset = queryset.order_by('tour_name')

                if 'direction' in self.request.GET:
                    direction = self.request.GET['direction']
                    if direction == 'ascending':
                        sort = f'{sort}'
                    if direction == 'desending':
                        sort = f'-{sort}'
                queryset = queryset.order_by(sort)

            # get user search results
            if 'q' in self.request.GET:
                query = self.request.GET.get("q")
                if not query:
                    messages.error(
                        self.request,
                        "You did not enter anything to search"
                        )
                queryset = queryset.filter(
                        Q(tour_name__icontains=query)
                        | Q(description__icontains=query)
                        )

            # search by category
            if 'category' in self.request.GET:
                categories = self.request.GET['category'].split(',')
                queryset = queryset.filter(category__name__in=categories)

        return queryset

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     query = self.request.GET.get("q")
    #     context['search_query'] = query
    #     sort = self.request.GET['sort']
    #     direction = self.request.GET['direction']
    #     sort_by = f'{sort}_{direction}'
    #     context['sort_by'] = sort_by
    #     return context


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
        context['reviews'] = paginator.get_page(page)
        context['page'] = page
        context['paginator'] = paginator
        context['review_form'] = ReviewForm()
        return context


class ReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Class to allow logged in users to update reviews """
    model = Review
    form_class = ReviewForm

    def form_valid(self, form):
        """
        Function to set signed in user
        as author of the review form to post
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        To get the review to be updated
        and ensure only the author can update it
        """
        review = self.get_object()
        if self.request.user == review.name:
            return True
        return False

    def get_success_url(self):
        """ On successful review update, return to post-detail view"""
        tour = self.object.tour
        return reverse_lazy('tour-detail', kwargs={'pk': tour.pk})


class ReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Allow user who created review to delete it.
    """
    model = Review()

    def test_func(self):
        """
        To get the review to be deleted
        and ensure only the author of the review can delete it
        """
        review = self.get_object()
        if self.request.user == review.name:
            return True
        return False

    def get_success_url(self):
        """ On successful review deletion, stay on same page"""
        tour = self.object.tour
        return reverse_lazy('tour-detail', kwargs={'pk': tour.pk})
