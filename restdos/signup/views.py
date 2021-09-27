from django.shortcuts import render

# Create your views here.
def details(request):
    return render(request, 'signup/details.html')


def business(request):
    return render(request, 'signup/business.html')


def restaurant(request):
    return render(request, 'signup/restaurant.html')


def billing(request):
    return render(request, 'signup/billing.html')
