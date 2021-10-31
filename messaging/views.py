from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings

from guests.models import Guest

from sms import send_sms
import stripe

# Create your views here.
@login_required
def compose_message(request):


    context = {
        'page': 'messaging',
    }
    return render(request, 'messaging/compose_message.html', context)


@login_required
def send_message(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    message = request.POST['message']
    filter = request.POST['filter']
    receipients = Guest.objects.filter(deleted=False, sms_marketing=True, user=request.user)
    mobiles = []
    for person in receipients:
        mobiles.append(person.mobile)
    receipients = receipients.count()
    

    if receipients == 0:
        messages.info(request, 'You either have no guests in your system or no guests with marketing sms enabled. Please add guests in order to send messages')
        return redirect('compose_message')

    sms_length = len(message)
    if sms_length <=160:
        sms_quantity = 1
    elif sms_length <=306:
        sms_quantity = 2
    else:
        sms_quantity = 3
    total_sms = sms_quantity * receipients
    sms_cost = total_sms * 0.08
    if sms_cost < 1:
        low_cost = True
        stripe_total = round(int(1) * 100)
    else:
        low_cost = False
        stripe_total = round(int(sms_cost) * 100)
    
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    context = {
        'page': 'messaging',
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'message': message,
        'filter': filter,
        'receipients': receipients,
        'sms_length': sms_length,
        'sms_quantity': sms_quantity,
        'sms_cost': sms_cost,
        'low_cost': low_cost,
        'mobiles': mobiles,
    }
    return render(request, 'messaging/send_message.html', context)


def message_success(request, message, mobiles):
    send_sms(
        message,
        'No Reply',
        mobiles,
        fail_silently=False
    )
    messages.success(request, 'Your payment was successful and you message campaign has been sent')
    return redirect('compose_message')