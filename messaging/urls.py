from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('compose_message', views.compose_message, name='compose_message'),
    path('preview_message', views.preview_message, name='preview_message'),
    path('send_message', views.send_message, name='send_message'),
]