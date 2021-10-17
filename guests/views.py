from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Guest
from bookings.models import Booking

from .forms import NotesForm
from .forms import PersonalInformationForm

# Create your views here.
def guests(request):

    guests = Guest.objects.filter(deleted=False)
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


    if request.method == 'POST':
        sms_marketing = False
        sms_transactional = False

        if 'sms_marketing' in request.POST:
            sms_marketing = True

        if 'sms_transactional' in request.POST:
            sms_transactional = True

        if 'first_name' in request.POST:
            form_data = {
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
    }
    return render(request, 'guests/guest_detail.html', context)


def add_guest(request):
    stars = range(5)

    personal_information_form = PersonalInformationForm()

    if request.method == 'POST':
        sms_marketing = False
        sms_transactional = False

        if 'sms_marketing' in request.POST:
            sms_marketing = True

        if 'sms_transactional' in request.POST:
            sms_transactional = True

        form_data = {
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
            return redirect('guest_detail', guest_id=form.id)
        else:
            print("failure")


    context = {
        'stars': stars,
        'personal_information_form': personal_information_form,
    }
    return render(request, 'guests/add_guest.html', context)


def delete_guest(request, guest_id):
    guest = get_object_or_404(Guest, pk=guest_id)
    guest.deleted = True
    guest.save(update_fields=['deleted'])
    return redirect('guests')