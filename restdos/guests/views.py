from django.shortcuts import render
from .models import Guest

# Create your views here.
def guests(request):
    guests = Guest.objects.all()

    for guest in guests:
        guest.unrating = 5 - guest.rating
        guest.rating = range(guest.rating)
        guest.unrating = range(guest.unrating)

    context = {
        'guests': guests,
    }

    return render(request, 'guests/guests.html', context)