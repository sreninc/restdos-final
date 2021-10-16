from django.shortcuts import render

# Create your views here.
def bookings(request):


    status = 'all'
    rating = range(5)

    context = {
        'status': status,
        'rating': rating,
    }
    return render(request, 'bookings/bookings.html', context)