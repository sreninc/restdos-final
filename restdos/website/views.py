from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'website/index.html')


def pricing(request):

    return render(request, 'website/pricing.html')


def contact(request):

    return render(request, 'website/contact.html')