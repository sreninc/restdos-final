from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.messaging, name='messaging'),
    path('compose_message/', views.compose_message, name='compose_message'),
    path('compose_transactional/', views.compose_transactional, name='compose_transactional'),
    path('compose_marketing/', views.compose_marketing, name='compose_marketing'),
    path('send_message/', views.send_message, name='send_message'),
    path('message_success/<message>/<mobiles>', views.message_success, name='message_success'),
]