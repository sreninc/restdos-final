from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import SignupForm

import stripe

# Create your views here.
def index(request):
    return render(request, 'website/index.html')


def pricing(request):

    return render(request, 'website/pricing.html')


def contact(request):

    return render(request, 'website/contact.html')


def signup(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    signup_plan =  'First Advantage'
    signup_monthly = 33
    stripe_total = round(signup_monthly * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,

    )


    signup_form = SignupForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    context = {
        'signup_plan': signup_plan,
        'signup_monthly': signup_monthly,
        'signup_form': signup_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    if not signup_plan:
        messages.error(request, 'You have not selected a signup plan')
        return redirect(reverse('pricing'))
    

    return render(request, 'website/signup.html', context)