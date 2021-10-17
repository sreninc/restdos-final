from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.guests, name='guests'),
    path('<int:guest_id>/', views.guest_detail, name='guest_detail'),
    path('add_guest/', views.add_guest, name='add_guest'),
    path('delete_guest/<int:guest_id>/', views.delete_guest, name='delete_guest'),
]
