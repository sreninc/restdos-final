from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookings, name='bookings'),
    path('add_booking/<int:guest_id>', views.add_booking, name='add_booking'),
    path('edit_booking/<int:booking_id>', views.edit_booking, name='edit_booking'),
]
