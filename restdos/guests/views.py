from django.shortcuts import render

# Create your views here.
def guests(request):
    return render(request, 'guests/guests.html')