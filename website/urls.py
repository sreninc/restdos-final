from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
    path('signup/<signup_plan>/<signup_monthly>/', views.signup, name='signup'),
    path('signup_email/<signup_plan>/<signup_monthly>/', views.signup_email, name='signup_email'),
    path('signup/success/', views.signup_success, name='signup_success'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('blog/', views.blog, name='blog'),
    path('guest_management/', views.guest_management, name='guest_management'),
    path('marketing/', views.marketing, name='marketing'),
    path('automated_messaging/', views.automated_messaging, name='automated_messaging'),
    path('booking_management/', views.booking_management, name='booking_management'),
    path('newsletter/', views.newsletter, name='newsletter'),
]
