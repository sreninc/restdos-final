from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<account_id>/', views.account, name='account'),
]
