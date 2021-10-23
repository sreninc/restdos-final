from django.shortcuts import render, redirect, reverse, get_object_or_404

from website.forms import SignupForm
from website.models import Signup

# Create your views here.
def account(request, account_id):
    signup = get_object_or_404(Signup, pk=account_id)

    if request.method == "POST":
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'mobile': request.POST['mobile'],
            'signup_plan': request.POST['signup_plan'],
            'signup_monthly': request.POST['signup_monthly'],
        }
        signup_form = SignupForm(form_data, instance=signup)
        if signup_form.is_valid():
            print('success')
            form = signup_form.save()
            return redirect('account', account_id=account_id)
        else:
            print('failure')
    else:
        form_data = {
            'first_name': signup.first_name,
            'last_name': signup.last_name,
            'email': signup.email,
            'mobile': signup.mobile,
            'signup_plan': signup.signup_plan,
            'signup_monthly': signup.signup_monthly,
        }

    signup_form = SignupForm(form_data)

    context = {
        'signup_form': signup_form,
    }
    return render(request, 'accounts/account.html', context)