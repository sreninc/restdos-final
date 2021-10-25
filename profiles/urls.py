from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('help', views.help, name='help'),
]