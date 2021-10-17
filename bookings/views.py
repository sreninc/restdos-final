from django.shortcuts import render, redirect, reverse, get_object_or_404

from guests.models import Guest
from .models import Booking

from .forms import BookingForm

# Create your views here.
def bookings(request):


    status = 'all'
    rating = range(5)

    context = {
        'status': status,
        'rating': rating,
    }
    return render(request, 'bookings/bookings.html', context)


def add_booking(request, guest_id):

    booking_form = BookingForm()

    if request.method == 'POST':
        form_data = {
            'guest_id': guest_id,
            'date': request.POST['date'],
            'time': request.POST['time'],
            'people': request.POST['people'],
            'rating': request.POST['rating'],
        }
        booking_form = BookingForm(form_data)
        if booking_form.is_valid():
            print('success')
            form = booking_form.save()
            return redirect('guest_detail', guest_id=guest_id)
        else:
            print('failure')

    context = {
        'booking_form': booking_form,
        'guest_id': guest_id,
    }

    return render(request, 'bookings/add_booking.html', context)