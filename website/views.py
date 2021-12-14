"""
Manages all the pages on the website
"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

from django.contrib.auth.models import User

import stripe


def index(request):
    """
    Show page on website
    """
    return render(request, 'website/index.html')


def newsletter(request):
    """
    Show page on website
    """
    email = request.POST['email-address']
    send_mail('Newsletter Signup', email, email, ['sean@restdos.com'])
    messages.success(request, f'You have successfully signed up to our \
                     newsletter with your email: {email}')
    template = request.META['HTTP_REFERER']
    return render(request, template)


def pricing(request):
    """
    Show page on website
    """
    signups = User.objects.count()
    secondary_string = 'at a permanently lower price for the next 10 customers'
    if signups <= 10:
        monthly = 33
        primary_string = " €33 a month"
        plan = 'First Advantage'
    elif signups <= 20:
        monthly = 50
        primary_string = ' €50 a month'
        plan = 'Second Advantage'
    elif signups <= 30:
        monthly = 67
        primary_string = ' €67 a month'
        plan = 'Third Advantage'
    elif signups <= 40:
        monthly = 80
        primary_string = ' €80 a month'
        plan = 'Final Advantage'
    else:
        monthly = 100
        primary_string = '100 a month'
        plan = 'Complete Advantage'
        secondary_string = 'including unlimited bookings and guests'

    template = 'website/pricing.html'
    context = {
        'monthly': monthly,
        'primary_string': primary_string,
        'secondary_string': secondary_string,
        'plan': plan,
    }
    return render(request, template, context)


def contact(request):
    """
    Show page on website
    """
    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        restaurant = request.POST['company']
        message = request.POST['message']
        message += ' ' + first_name + ' ' + last_name + ' '
        message += restaurant + ' ' + email
        send_mail('New Message', message, email, ['sean@restdos.com'])
        messages.success(request, 'You have successfully sent a message to \
                         us. We will reply to your email: {email}')
    return render(request, 'website/contact.html')


def signup(request, signup_plan, signup_monthly):
    """
    Show page on website
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    stripe_total = round(int(signup_monthly) * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    context = {
        'signup_plan': signup_plan,
        'signup_monthly': signup_monthly,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    if not signup_plan:
        messages.error(request, 'You have not selected a signup plan')
        return redirect(reverse('pricing'))

    if request.method == 'POST':
        return redirect('account_signup')

    return render(request, 'website/signup.html', context)


def signup_success(request):
    """
    Show page on website
    """
    return render(request, 'website/new_user.html')


def terms(request):
    """
    Show page on website
    """
    return render(request, 'website/terms_and_conditions.html')


def privacy(request):
    """
    Show page on website
    """
    return render(request, 'website/privacy.html')


def blog(request):
    """
    Show page on website
    """
    return render(request, 'website/blog.html')


def demo(request):
    """
    Show page on website
    """
    return render(request, 'website/demo.html')


def guest_crm(request):
    """
    Show page on website
    """
    return render(request, 'website/guest_crm.html')
    

def messaging(request):
    """
    Show page on website
    """
    return render(request, 'website/messaging.html')
        

def booking_management(request):
    """
    Show page on website
    """
    return render(request, 'website/booking_management.html')
    

def data(request):
    """
    Show page on website
    """
    return render(request, 'website/data.html')