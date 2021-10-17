from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.guests, name='guests'),
    path('<int:guest_id>/', views.guest_detail, name='guest_detail'),
    path('<int:guest_id>/add_booking/', views.add_booking, name='add_booking'),
    path('add_guest/', views.add_guest, name='add_guest'),
    path('update_guest/<int:guest_id>', views.update_guest, name='update_guest'),
    path('delete_guest/<int:guest_id>/', views.delete_guest, name='delete_guest'),
]
