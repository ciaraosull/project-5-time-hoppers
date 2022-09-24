"""Views for Subscibers form & Newsletter"""
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
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

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                'Test Title',
                'Test Body',
                settings.DEFAULT_FROM_EMAIL,
                ['ciaraosull@gmail.com'],
                fail_silently=False,  # if email saved is incorrect
            )
            messages.success(request, 'Newsletter Sent Successfully')
            return redirect('newsletter')
    else:
        form = NewsletterForm()

    context = {
        'form': form,
    }
    return render(request, 'newsletters/newsletter.html', context)
