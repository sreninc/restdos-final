from django.shortcuts import render, redirect, reverse, get_object_or_404


from guests.models import Guest
from .models import Booking

from .forms import BookingForm

# Create your views here.
def bookings(request):

    bookings = Booking.objects.all()
    for booking in bookings:
        booking.unrating = 5 - booking.rating
        booking.rating = range(booking.rating)
        booking.unrating = range(booking.unrating)
        booking.status = booking.get_status_display()

    status = 'all'

    context = {
        'status': status,
        'bookings': bookings,
    }

    return render(request, 'bookings/bookings.html', context)


def add_booking(request, guest_id):

    booking_form = BookingForm()

    if request.method == 'POST':
        form_data = {
            'guest': guest_id,
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