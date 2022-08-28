""" URLS for Basket App"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_basket, name='view-basket'),
    path('add/<item_id>/', views.add_to_basket, name='add-to-basket'),
]
