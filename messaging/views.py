from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from sms import send_sms

# Create your views here.
@login_required
def compose_message(request):
    send_sms(
        'Here is the message',
        '+12065550100',
        ['+441134960000'],
        fail_silently=False
    )

    context = {
        'page': 'messaging',
    }
    return render(request, 'messaging/compose_message.html', context)


@login_required
def preview_message(request):

    context = {
        'page': 'messaging',
    }
    return render(request, 'messaging/preview_message.html', context)


@login_required
def send_message(request):

    context = {
        'page': 'messaging',
    }
    return render(request, 'messaging/send_message.html', context)