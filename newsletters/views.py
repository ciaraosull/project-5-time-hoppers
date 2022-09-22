"""Views for Subscibers form & Newsletter"""
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubsciberForm, NewsletterForm


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


def newsletter(request):
    """Newsletter Form View"""
    form = NewsletterForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletters/newsletter.html', context)
