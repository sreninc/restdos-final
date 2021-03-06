from datetime import datetime, timedelta
from django.shortcuts import render
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

from guests.models import Guest
from bookings.models import Booking



# Create your views here.
@login_required
def dashboard(request,
              filter=7):

    filter = int(filter)
    start_date = datetime.now() - timedelta(days=filter)
    start_date = start_date.strftime('%Y-%m-%d') 
    end_date = datetime.now().strftime('%Y-%m-%d') 

    guests = Guest.objects.filter(deleted=False, user=request.user)
    bookings = Booking.objects.filter(
        deleted=False,
        user=request.user,
        date__range=[start_date, end_date])

    total_guests = 0
    total_bookings = 0
    total_sales = 0
    no_show_percentage = 0
    completed_percentage = 0
    avg_booking_value = 0

    if guests:
        total_guests = guests.count()

    if bookings:
        total_bookings = bookings.count()

    if bookings.filter(status='COM'):
        total_sales = bookings.filter(status='COM').aggregate(Sum('booking_value'))['booking_value__sum']
        completed_percentage = (bookings.filter(status='COM').count() / bookings.count()) * 100
        avg_booking_value = bookings.filter(status='COM').aggregate(Sum('booking_value'))['booking_value__sum'] / bookings.filter(status='COM').count()
        
    if bookings.filter(status='NOS'):
        no_show_percentage = (bookings.filter(status='NOS').count() / bookings.count()) * 100

    start_filter_date = datetime.now() - timedelta(days=filter)
    start_date = start_filter_date.day
    start_month = start_filter_date.strftime('%b')
    end_month = datetime.now().strftime('%b')
    end_date = datetime.now().day
    page_description = start_month + ' ' + ordinal(start_date) + ' - ' + end_month + ' ' + ordinal(end_date)

    stats = {
        'total_guests': {
            'name': 'Total Guests',
            'value': total_guests,
        },
        'total_bookings': {
            'name': 'Total Bookings',
            'value': total_bookings,
        },
        'total_sales': {
            'name': 'Total Sales',
            'value': total_sales,
        },
        'no_show_percentage': {
            'name': 'No-Show %',
            'value': no_show_percentage,
        },
        'completed_percentage': {
            'name': 'Completed %',
            'value': completed_percentage,
        },
        'avg_booking_value': {
            'name': 'Average Booking Value',
            'value': avg_booking_value,
        },
    }

    context = {
        'stats': stats,
        'page': 'dashboard',
        'filter': filter,
        'page_description': page_description,
    }
    return render(request, 'reports/dashboard.html', context)


## From https://leancrew.com/all-this/2020/06/ordinals-in-python/
def ordinal(n):
  s = ('th', 'st', 'nd', 'rd') + ('th',)*10
  v = n%100
  if v > 13:
    return f'{n}{s[v%10]}'
  else:
    return f'{n}{s[v]}'