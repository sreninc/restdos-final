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
    path('privacy/', views.privacy, name='privacy'),
    path('blog/', views.blog, name='blog'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('demo/', views.demo, name='demo'),
    path('guest_crm/', views.guest_crm, name='guest_crm'),
    path('marketing_messaging/', views.marketing_messaging, name='marketing_messaging'),
    path('booking_management/', views.booking_management, name='booking_management'),
    path('data/', views.data, name='data'),
]