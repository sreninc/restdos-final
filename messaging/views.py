from django.shortcuts import render

# Create your views here.
def compose_message(request):
    return render(request, 'messaging/compose_message.html')


def preview_message(request):
    return render(request, 'messaging/preview_message.html')


def send_message(request):
    return render(request, 'messaging/send_message.html')