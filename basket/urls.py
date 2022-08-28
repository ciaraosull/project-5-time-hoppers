""" URLS for Basket App"""
from django.urls import path
from basket.views import BasketView

urlpatterns = [
    path('', BasketView.as_view(), name='basket'),
]
