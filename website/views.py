from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

from django.contrib.auth.models import User

import stripe

# Create your views here.
def index(request):
    return render(request, 'website/index.html')


def newsletter(request):
    email = request.POST['email-address']
    send_mail('Newsletter Signup', email, email, ['sean@restdos.com'])
    messages.success(request,f'You have successfully signed up to our newsletter with your email: {email}')
    template = request.META['HTTP_REFERER']
    return render(request, 'website/index.html')


def pricing(request):
    signups = User.objects.count()
    secondary_string = 'at a permanently reduced price for the next 10 customers'
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
    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        restaurant = request.POST['company']
        message = request.POST['message']
        message = message + ' ' + first_name + ' ' + last_name + ' ' + restaurant + ' ' + email
        send_mail('New Message', message, email, ['sean@restdos.com'])
        messages.success(request,f'You have successfully sent a message to us. We will reply to your email: {email}')
    return render(request, 'website/contact.html')

def signup_email(request, signup_plan, signup_monthly):

    if request.method == 'POST':
        if User.objects.filter(email=request.POST['email']):
            messages.warning(request, 'A user with that email already exists.')
        else:
            return redirect('signup', signup_plan=signup_plan, signup_monthly=signup_monthly)



    context = {
        'signup_plan': signup_plan,
        'signup_monthly': signup_monthly,
    }
    return render(request, 'website/signup_email.html', context)

def signup(request, signup_plan, signup_monthly):
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
    return render(request, 'website/new_user.html') 


def terms(request):
    return render(request, 'website/terms_and_conditions.html')


def privacy(request):
    return render(request, 'website/privacy.html')


def blog(request):
    return render(request, 'website/blog.html')


def guest_management(request):
    return render(request, 'website/guest_management.html')


def marketing(request):
    return render(request, 'website/marketing.html')


def automated_messaging(request):
    return render(request, 'website/automated_messaging.html')


def booking_management(request):
    return render(request, 'website/booking_management.html')