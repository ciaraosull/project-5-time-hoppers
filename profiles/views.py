"""Views to show the Profile Page"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from checkout.models import Order
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile


@login_required
def profile(request):
    """
    Return profile update image form &
    user update details form to template &
    pre-populate with the users details,
    if both valid then save
    """
    user_profile = get_object_or_404(Profile, user=request.user)
    order = Order.objects.all()

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,  # file data from image being uploaded
            instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')  # get request sent after reload

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    orders = user_profile.orders.all()
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'orders': orders,
        'order': order,
    }
    return render(request, 'profiles/profile-page.html', context)
