from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Guest
from bookings.models import Booking

from .forms import GuestDetailsForm
from .forms import PersonalInformationForm

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
            messages.success(request, f'Searched for "{query}" successfully.')


    

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

    form_data = {
        'first_name': guest.first_name,
        'last_name': guest.last_name,
        'email': guest.email,
        'mobile': guest.mobile,
        'dob': guest.dob,
        'rating': guest.rating,
        'service_notes': guest.service_notes,
        'kitchen_notes': guest.kitchen_notes,
        'allergen_notes': guest.allergen_notes,
        'sms_marketing': guest.sms_marketing,
        'sms_transactional': guest.sms_transactional,
    }
    guest_details_form = GuestDetailsForm(form_data)

    context = {
        'guest': guest,
        'guest_details_form': guest_details_form,
    }

    return render(request, 'guests/guest_detail.html', context)


def add_guest(request):
    stars = range(5)

    personal_information_form = PersonalInformationForm()

    if request.method == "POST":
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'mobile': request.POST['mobile'],
            'dob': request.POST['dob'],
            'rating': request.POST['rating'],
            'sms_marketing': request.POST['sms_marketing'],
            'sms_transactional': request.POST['sms_transactional'],
        }
        personal_information_form = PersonalInformationForm(form_data)
        if personal_information_form.is_valid():
            personal_information_form.save()
            print("success")
        else:
            print("failure")


    context = {
        'stars': stars,
        'personal_information_form': personal_information_form,
    }
    return render(request, 'guests/add_guest.html', context)


def add_booking(request, guest_id):

    guest = get_object_or_404(Guest, pk=guest_id)
    guest.unrating = 5 - guest.rating
    guest.rating = range(guest.rating)
    guest.unrating = range(guest.unrating)

    context = {
        'guest': guest
    }

    return render(request, 'guests/add_booking.html', context)

