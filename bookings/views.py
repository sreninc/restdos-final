from django.shortcuts import render, redirect, reverse, get_object_or_404
from datetime import datetime
from django.contrib.auth.decorators import login_required

from guests.models import Guest
from .models import Booking

from .forms import BookingForm

# Create your views here.
@login_required
def bookings(request, status='all', date=datetime.now().strftime('%Y-%m-%d')):
    """
    View to generate all the bookings the user should see. Default filters to today and all bookings
    """

    if status == 'all':
        bookings = Booking.objects.filter(deleted=False, date=date, user=request.user)
    else:
        bookings = Booking.objects.filter(deleted=False, date=date, status=status, user=request.user)

    bookings = bookings.order_by('time')

    for booking in bookings:
        booking.unrating = 5 - booking.rating # rating is used to generate stars on booking page
        booking.rating = range(booking.rating)
        booking.unrating = range(booking.unrating)
        booking.status = booking.get_status_display()
        booking.time = booking.time.strftime("%H:%M")

    context = {
        'status': status,
        'bookings': bookings,
        'page': 'bookings',
        'date': date,
        'status': status,
    }

    return render(request, 'bookings/bookings.html', context)

@login_required
def add_booking(request, guest_id):
    """
    View to allow the user to add a booking
    """

    booking_form = BookingForm(initial={'user': request.user.id })
    guest = get_object_or_404(Guest, pk=guest_id, deleted=False, user=request.user)

    if request.method == 'POST':
        form_data = {
            'user': request.user,
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
        'guest': guest,
    }

    return render(request, 'bookings/add_booking.html', context)


def edit_booking(request, booking_id):
    """
    View to allow the user to see a bookings details and edit them
    """

    booking = get_object_or_404(Booking, pk=booking_id, deleted=False, user=request.user)

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
            'user': request.user,
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
            return redirect('bookings', status=request.POST['status'], date=request.POST['date'], )
        else:
            print('failure')

    template = 'bookings/edit_booking.html'
    context = {
        'booking_form': booking_form,
        'booking_id': booking_id,
        'booking': booking,
    }
    return render(request, template, context)

@login_required
def delete_booking(request, booking_id):
    """
    View to allow the booking to be deleted
    """

    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    booking.deleted = True
    booking.save(update_fields=['deleted'])
    return redirect('bookings')