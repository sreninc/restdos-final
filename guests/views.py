from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum

from datetime import datetime

from .models import Guest
from bookings.models import Booking

from .forms import NotesForm
from .forms import PersonalInformationForm

# Create your views here.
@login_required
def guests(request):
    """
    view to show all guests to user
    """

    empty = {
        'cause': 'No Guests Available',
        'context': 'You can add a guest by clicking the button below.',
        'action': 'Add Guest',
    }

    guests = Guest.objects.filter(deleted=False, user=request.user)
    guests = guests.order_by('first_name', 'last_name')
    query = None

    if request.GET:
        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.info(request, "You didn't enter any search criteria!")
                return redirect(reverse('guests'))

            queries = Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(mobile__icontains=query) | Q(email__icontains=query)
            guests = guests.filter(queries)

            if guests.count() == 1:
                return redirect('guest_detail', guest_id=guests.first().id)
            elif guests.count() == 0:
                messages.warning(request, f'Your search query for "{query}" returned no results.')
            else:
                messages.success(request, f'Search for "{query}" returned "{guests.count()}" results.')

    for guest in guests:
        guest.unrating = 5 - guest.rating
        guest.rating = range(guest.rating)
        guest.unrating = range(guest.unrating)

    context = {
        'guests': guests,
        'search_term': query,
        'page': 'guests',
        'empty': empty,
    }

    return render(request, 'guests/guests.html', context)

@login_required
def guest_detail(request, guest_id):
    """
    view to show the guest detail page to users and allow them to update it
    """

    guest = get_object_or_404(Guest, pk=guest_id, user=request.user, deleted=False)
    bookings = Booking.objects.filter(guest=guest_id, deleted=False, user=request.user)

    total_bookings = 0
    total_sales = 0
    no_show_percentage = 0
    completed_percentage = 0
    avg_booking_value = 0

    if bookings:
        total_bookings = bookings.count()
        for booking in bookings:
            booking.unrating = 5 - booking.rating
            booking.rating = range(booking.rating)
            booking.unrating = range(booking.unrating)
            booking.status = booking.get_status_display()
            booking.written_date = booking.date.strftime("%a %d %b")


        if bookings.filter(status='COM'):
            total_sales = bookings.filter(status='COM').aggregate(Sum('booking_value'))['booking_value__sum']
            completed_percentage = (bookings.filter(status='COM').count() / bookings.count()) * 100
            avg_booking_value = bookings.filter(status='COM').aggregate(Sum('booking_value'))['booking_value__sum'] / bookings.count()
        
        if bookings.filter(status='NOS'):
            no_show_percentage = (bookings.filter(status='NOS').count() / bookings.count()) * 100

    empty = {
        'cause': 'No Bookings Yet',
        'context': 'This guest does not have any bookings yet. Click the button below to add a booking.',
        'action': 'Add Booking',
    }
        

    guest_age = (datetime.now() - datetime.combine(guest.guest_since, datetime.min.time())).days
    # Calculating years
    years = guest_age // 365

    # Calculating months
    months = (guest_age - years * 365) // 30

    # Calculating days
    days = (guest_age - years * 365 - months*30)

    guest_age = str(years) + "Y " + str(months) + "M " + str(days) + "D"

    stats = {
        'guest_age': {
            'name': 'Guest Age',
            'value': guest_age,
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


    if request.method == 'POST':
        sms_marketing = False
        sms_transactional = False

        if 'sms_marketing' in request.POST:
            sms_marketing = True

        if 'sms_transactional' in request.POST:
            sms_transactional = True

        if 'first_name' in request.POST:
            form_data = {
                'user': request.user,
                'first_name': request.POST['first_name'],
                'last_name': request.POST['last_name'],
                'email': request.POST['email'],
                'mobile': request.POST['mobile'],
                'dob': request.POST['dob'],
                'rating': request.POST['rating'],
                'sms_marketing': sms_marketing,
                'sms_transactional': sms_transactional,
            }
            personal_information_form = PersonalInformationForm(form_data, instance=guest)
            if personal_information_form.is_valid():
                form = personal_information_form.save()
                return redirect('guest_detail', guest_id=form.id)
            else:
                print("failure")
        else:
            form_data = {
                'user': request.user,
                'service_notes': request.POST['service_notes'],
                'kitchen_notes': request.POST['kitchen_notes'],
                'allergen_notes': request.POST['allergen_notes'],
            }
            notes_form = NotesForm(form_data, instance=guest)
            if notes_form.is_valid():
                form = notes_form.save()
                return redirect('guest_detail', guest_id=form.id)
    else:
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
        personal_information_form = PersonalInformationForm(form_data)
        notes_data = {
            'service_notes': guest.service_notes, 
            'kitchen_notes': guest.kitchen_notes, 
            'allergen_notes': guest.allergen_notes,
        }
        notes_form = NotesForm(notes_data)


    context = {
        'guest': guest,
        'personal_information_form': personal_information_form,
        'notes_form': notes_form,
        'stats': stats,
        'bookings': bookings,
        'page': 'guests',
        'empty': empty,
    }
    return render(request, 'guests/guest_detail.html', context)

@login_required
def add_guest(request):
    """
    view to allow the user to add a guest
    """
    stars = range(5)

    personal_information_form = PersonalInformationForm(initial={'user': request.user.id })

    if request.method == 'POST':
        sms_marketing = False
        sms_transactional = False

        if 'sms_marketing' in request.POST:
            sms_marketing = True

        if 'sms_transactional' in request.POST:
            sms_transactional = True

        print(request.user)
        print(request.user.id)

        form_data = {
            'user': request.user,
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'mobile': request.POST['mobile'],
            'dob': request.POST['dob'],
            'rating': request.POST['rating'],
            'sms_marketing': sms_marketing,
            'sms_transactional': sms_transactional,
        }
        personal_information_form = PersonalInformationForm(form_data)
        if personal_information_form.is_valid():
            form = personal_information_form.save()
            messages.success(request, f'Guest was successfully added.')
            return redirect('guest_detail', guest_id=form.id)
        else:
            messages.warning(request, 'There was an error creating the guest. Please try again or contact us.')
            return reverse('add_guest')


    context = {
        'stars': stars,
        'personal_information_form': personal_information_form,
        'page': 'guests',
    }
    return render(request, 'guests/add_guest.html', context)

@login_required
def delete_guest(request, guest_id):
    guest = get_object_or_404(Guest, pk=guest_id, user=request.user)
    guest.deleted = True
    guest.save(update_fields=['deleted'])
    return redirect('guests')