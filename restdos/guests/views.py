from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Guest
from bookings.models import Booking

# Create your views here.
def guests(request):

    guests = Guest.objects.all()
    query = None

    if request.GET:
        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('guests'))

            queries = Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(mobile__icontains=query) | Q(email__icontains=query)
            guests = guests.filter(queries)


    

    for guest in guests:
        guest.unrating = 5 - guest.rating
        guest.rating = range(guest.rating)
        guest.unrating = range(guest.unrating)

    context = {
        'guests': guests,
        'search_term': query,
    }

    return render(request, 'guests/guests.html', context)


def guest_detail(request, guest_id):

    guest = get_object_or_404(Guest, pk=guest_id)
    guest.unrating = 5 - guest.rating
    guest.rating = range(guest.rating)
    guest.unrating = range(guest.unrating)

    context = {
        'guest': guest
    }

    return render(request, 'guests/guest_detail.html', context)


def add_booking(request, guest_id):

    guest = get_object_or_404(Guest, pk=guest_id)
    guest.unrating = 5 - guest.rating
    guest.rating = range(guest.rating)
    guest.unrating = range(guest.unrating)

    context = {
        'guest': guest
    }

    return render(request, 'guests/add_booking.html', context)

