from django.shortcuts import render

# Create your views here.
def compose_message(request):

    context = {
        'page': 'messaging',
    }
    return render(request, 'messaging/compose_message.html', context)


def preview_message(request):

    context = {
        'page': 'messaging',
    }
    return render(request, 'messaging/preview_message.html', context)


def send_message(request):

    context = {
        'page': 'messaging',
    }
    return render(request, 'messaging/send_message.html', context)