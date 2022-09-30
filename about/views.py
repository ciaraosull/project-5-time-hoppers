"""
Imports for About Us Views
"""
from django.views.generic import ListView
from .models import StaffMember


class AboutUsListView(ListView):
    """Class to show the Staff in list view on About Us Page """
    model = StaffMember
    template_name = 'about/about_us.html'
    context_object_name = 'staff'
    ordering = ['-date_added']
