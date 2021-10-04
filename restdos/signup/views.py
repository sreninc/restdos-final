from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import SignupForm


# Create your views here.
def details(request):
    return render(request, 'signup/details.html')


def business(request):
    return render(request, 'signup/business.html')


def restaurant(request):
    return render(request, 'signup/restaurant.html')


def billing(request):
    signup_plan =  'First Advantage'
    signup_monthly = 33

    signup_form = SignupForm()

    context = {
        'signup_plan': signup_plan,
        'signup_monthly': signup_monthly,
        'signup_form': signup_form,
    }

    if not signup_plan:
        messages.error(request, 'You have not selected a signup plan')
        return redirect(reverse('pricing'))
    

    return render(request, 'signup/billing.html', context)
