from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.guests, name='guests'),
    path('<int:guest_id>/', views.guest_detail, name='guest_detail'),
    path('<int:guest_id>/add_booking/', views.add_booking, name='add_booking'),
]
