"""
View to manage marketing messaging within app
"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings

from sms import send_sms
import stripe

from guests.models import Guest
from bookings.models import Booking
from .models import MessagingCampaign

from .forms import MessagingCampaignForm


@login_required
def messaging(request):

    guests = Guest.objects.filter(deleted=False, user=request.user).count()
    marketing_guests = Guest.objects.filter(deleted=False, user=request.user, sms_marketing=True).count()
    transactional_guests = Guest.objects.filter(deleted=False, user=request.user, sms_transactional=True).count()

    context = {
        'page': 'messaging',
        'guests': guests,
        'marketing_guests': marketing_guests,
        'transactional_guests': transactional_guests,
    }
    return render(request, 'messaging/index.html', context)


@login_required
def compose_message(request):
    """
    Function to load compose message page
    """

    title = 'Compose SMS'
    description = 'Compose a marketing SMS to your guests and select who you would like to send it to'
    filters = {
        'all_guests': {
            'name': 'All Guests',
            'value': 'all',
        },
        'booked_guests': {
            'name': 'Booked Guests',
            'value': 'booked',
        },
    }

    context = {
        'page': 'messaging',
        'title': title,
        'description': description,
        'filters': filters,
    }
    return render(request, 'messaging/compose_message.html', context)


@login_required
def compose_marketing(request):

    title = 'Compose Marketing SMS'
    description = 'Compose a marketing SMS to your guests with marketing consent and select who you would like to send it to'
    filters = {
        'all_guests': {
            'name': 'All Guests',
            'value': 'all',
        },
        'booked_guests': {
            'name': 'Booked Guests',
            'value': 'booked',
        },
    }

    context = {
        'page': 'messaging',
        'title': title,
        'description': description,
        'filters': filters,
    }
    return render(request, 'messaging/compose_marketing.html', context)


@login_required
def compose_transactional(request):

    title = 'Compose Transactional SMS'
    description = 'Compose a transactional SMS relevant to your guests bookings.'
    filters = {
        'booked_guests': {
            'name': 'Booked Guests',
            'value': 'booked',
        },
    }

    context = {
        'page': 'messaging',
        'title': title,
        'description': description,
        'filters': filters,
    }
    return render(request, 'messaging/compose_transactional.html', context)


@login_required
def send_message(request):
    """
    Generates message details and sends message once payment is confirmed
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    guests = Guest.objects.filter(deleted=False, user=request.user)
    if guests.count() == 0:
        messages.info(request, 'You have no guests in your system. ' +
                      'Please add guests in order to send messages')
        return redirect('messaging')

    if guests.filter(sms_marketing=True).count() == 0:
        messages.info(request, 'You have no guests in your system ' +
                      'with marketing sms enabled. ' +
                      'Please add consent in order to send messages')
        return redirect('messaging')

    message = request.POST['message']
    recipient_filter = request.POST['filter']

    if recipient_filter == 'all':
        receipients = Guest.objects.filter(
            deleted=False, sms_marketing=True, user=request.user)
    elif recipient_filter == 'booked':
        receipients = Guest.objects.filter(
            booking__user=request.user, booking__deleted=False, deleted=False, sms_marketing=True)
    mobiles = []
    for person in receipients:
        mobiles.append(person.mobile)
    receipients = receipients.count()

    sms_length = len(message)
    if sms_length <= 160:
        sms_quantity = 1
    elif sms_length <= 306:
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

    form_data = {
        'filter': recipient_filter,
        'message': message,
        'recipients': receipients,
        'sms_length': sms_length,
        'sms_quantity': sms_quantity,
        'sms_cost': sms_cost,
        'low_cost': low_cost,
    }
    campaign_form = MessagingCampaignForm(form_data)
    if campaign_form.is_valid():
        campaign_form.save()
        messages.success(request, 'success')
    else:
        messages.warning(request, 'error')

    context = {
        'page': 'messaging',
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'message': message,
        'filter': recipient_filter,
        'receipients': receipients,
        'sms_length': sms_length,
        'sms_quantity': sms_quantity,
        'sms_cost': sms_cost,
        'low_cost': low_cost,
        'mobiles': mobiles,
    }
    return render(request, 'messaging/send_message.html', context)


def message_success(request, message, mobiles):
    """
    When the message is successful let the user know
    """
    send_sms(
        message,
        'No Reply',
        mobiles,
        fail_silently=False
    )
    messages.success(request, 'Your payment was successful and you message ' +
                     'campaign has been sent')
    return redirect('messaging')