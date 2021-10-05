from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import SignupForm


# Create your views here.
def billing(request):
    signup_plan =  'First Advantage'
    signup_monthly = 33

    signup_form = SignupForm()

    context = {
        'signup_plan': signup_plan,
        'signup_monthly': signup_monthly,
        'signup_form': signup_form,
        'stripe_public_key': 'sk_test_51JhGLYFayXVaCl2yUFk4s9rJ1K71cjinE8JRQbdISSp9HWtyAwHY1HTEDxkKyaS1JL3bCmoKLzh6BJCX6BSyYDfo00j4hZWAgR',
        'client_secret': 'test client secret',
    }

    if not signup_plan:
        messages.error(request, 'You have not selected a signup plan')
        return redirect(reverse('pricing'))
    

    return render(request, 'signup/billing.html', context)
