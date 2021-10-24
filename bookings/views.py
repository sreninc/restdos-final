from django.shortcuts import render, redirect, reverse, get_object_or_404


from guests.models import Guest
from .models import Booking

from .forms import BookingForm

# Create your views here.
def bookings(request):

    bookings = Booking.objects.filter(deleted=False)
    for booking in bookings:
        booking.unrating = 5 - booking.rating
        booking.rating = range(booking.rating)
        booking.unrating = range(booking.unrating)
        booking.status = booking.get_status_display()

    status = 'all'

    context = {
        'status': status,
        'bookings': bookings,
        'page': 'bookings',
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
            'status': request.POST['status'],
            'booking_value': request.POST['booking_value'],
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
        'page': 'bookings',
    }

    return render(request, 'bookings/add_booking.html', context)


def edit_booking(request, booking_id):

    booking = get_object_or_404(Booking, pk=booking_id)

    booking_form = BookingForm()

    form_data = {
        'guest': booking.guest,
        'date': booking.date,
        'time': booking.time,
        'people': booking.people,
        'rating': booking.rating,
        'status': booking.status,
        'booking_value': booking.booking_value,
    }

    booking_form = BookingForm(form_data)

    if request.method == 'POST':
        form_data = {
            'guest': request.POST['guest'],
            'date': request.POST['date'],
            'time': request.POST['time'],
            'people': request.POST['people'],
            'rating': request.POST['rating'],
            'status': request.POST['status'],
            'booking_value': request.POST['booking_value'],
        }
        booking_form = BookingForm(form_data, instance=booking)
        if booking_form.is_valid():
            print('success')
            form = booking_form.save()
        else:
            print('failure')

    template = 'bookings/edit_booking.html'
    context = {
        'booking_form': booking_form,
        'booking_id': booking_id,
    }
    return render(request, template, context)


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    booking.deleted = True
    booking.save(update_fields=['deleted'])
    return redirect('bookings')