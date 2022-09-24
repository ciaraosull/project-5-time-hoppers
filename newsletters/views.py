"""Views for Subscibers form & Newsletter"""
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
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
            summernote_message = message
            plain_message = strip_tags(summernote_message)  # strip html tags
            from_email = ''  # using gmail in settings.py
            to_email = 'ciaraosull@gmail.com'
            bcc_email = 'bcc@example.com'

            email = EmailMessage(
                title,
                plain_message,
                from_email,
                [to_email],
                [bcc_email],
            )
            email.send(fail_silently=False)

            messages.success(request, 'Newsletter Sent Successfully')
            return redirect('newsletter')
    else:
        form = NewsletterForm()

    context = {
        'form': form,
    }
    return render(request, 'newsletters/newsletter.html', context)
