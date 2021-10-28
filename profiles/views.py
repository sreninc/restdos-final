from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from website.forms import SignupForm


def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(User, username=request.user)

    if request.method == 'POST':
        form = SignupForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = SignupForm()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'page': 'account',
    }

    return render(request, template, context)


def help(request):

    context = {
        'page': 'help',
    }
    return render(request, 'profiles/help.html', context)