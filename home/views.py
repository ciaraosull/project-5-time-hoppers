"""
Imports for Home Views
"""

from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib import messages
from newsletters.forms import SubsciberForm


class HomeView(TemplateView):
    """ Class-based view to return home page """
    template_name = 'home/index.html'


def subscribe(request):
    """Subscribers Form View"""
    if request.method == 'POST':
        form = SubsciberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription Successful')
            return redirect('/')
    else:
        form = SubsciberForm()
    context = {
        'form': form,
    }
    return render(request, 'home/index.html', context)
