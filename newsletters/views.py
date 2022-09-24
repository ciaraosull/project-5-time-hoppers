"""Views for Subscibers form & Newsletter"""
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core import mail
from django.utils.html import strip_tags
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
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')

            subject = title
            html_message = message
            plain_message = strip_tags(html_message)
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = 'to@example.com'

            mail.send_mail(subject, plain_message, from_email, [to_email])

            messages.success(request, 'Newsletter Sent Successfully')
            return redirect('newsletter')
    else:
        form = NewsletterForm()

    context = {
        'form': form,
    }
    return render(request, 'newsletters/newsletter.html', context)
