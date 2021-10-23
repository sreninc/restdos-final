from django.shortcuts import render

from guests.models import Guest
from bookings.models import Booking



# Create your views here.
def dashboard(request):

    guests = Guest.objects.all()
    bookings = Booking.objects.all()

    total_guests = guests.count()
    total_bookings = bookings.count()
    total_sales = 0
    no_show_percentage = 0
    completed_percentage = 0
    avg_booking_value = 0

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