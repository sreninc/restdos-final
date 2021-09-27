from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('details/', views.details, name='details'),
    path('business/', views.business, name='business'),
    path('restaurant/', views.restaurant, name='restaurant'),
    path('billing/', views.billing, name='billing'),
]
