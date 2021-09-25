from django.shortcuts import render, get_object_or_404
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


def guest_detail(request, guest_id):

    guest = get_object_or_404(Guest, pk=guest_id)
    guest.unrating = 5 - guest.rating

    context = {
        'guest': guest
    }

    return render(request, 'guests/guest_detail.html', context)