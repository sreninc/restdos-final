from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
    path('signup/<signup_plan>/<signup_monthly>/', views.signup, name='signup'),
    path('signup/success/', views.signup_success, name='signup_success'),
    path('terms/', views.terms, name='terms'),
]
