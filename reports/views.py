from django.shortcuts import render
from django.db.models import Sum

from guests.models import Guest
from bookings.models import Booking



# Create your views here.
def dashboard(request):

    guests = Guest.objects.all()
    bookings = Booking.objects.all()
    print(bookings)
    print(type(bookings.first().booking_value))
    print(bookings.filter(status='CON'))

    total_guests = guests.count()
    total_bookings = bookings.count()
    total_sales = bookings.filter(status='COM').aggregate(Sum('booking_value'))['booking_value__sum']
    no_show_percentage = (bookings.filter(status='NOS').count() / bookings.count()) * 100
    completed_percentage = (bookings.filter(status='COM').count() / bookings.count()) * 100
    avg_booking_value = bookings.filter(status='COM').aggregate(Sum('booking_value'))['booking_value__sum'] / bookings.count()

    stats = {
        'total_guests': total_guests,
        'total_bookings': total_bookings,
        'total_sales': total_sales,
        'no_show_percentage': no_show_percentage,
        'completed_percentage': completed_percentage,
        'avg_booking_value': avg_booking_value,
    }

    context = {
        'stats': stats,
        'page': 'dashboard',
    }
    return render(request, 'reports/dashboard.html', context)