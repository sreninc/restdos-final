"""
Manages all the pages on the website
"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

from django.contrib.auth.models import User

import stripe


def index(request):
    """
    Show page on website
    """
    header = {
        'image': '      ',
        'image_alt': 'People working on laptops',
        'title_first': 'Grow your',
        'title_second': 'restaurant revenue',
        'explainer': 'Take control of your guest database to grow your restaurant. Powerful messaging, complete guest management and effective booking management that works for you.',
        'cta_one_url': 'pricing',
        'cta_one_label': 'Get Started',
        'cta_two_url': 'live_demo',
        'cta_two_label': 'Live Demo',
    }

    context = {
        'header': header,
    }

    return render(request, 'website/index.html', context)


def newsletter(request):
    """
    Show page on website
    """
    email = request.POST['email-address']
    send_mail('Newsletter Signup', email, email, ['sean@restdos.com'])
    messages.success(request, f'You have successfully signed up to our \
                     newsletter with your email: {email}')
    template = request.META['HTTP_REFERER']
    return render(request, template)


def pricing(request):
    """
    Show page on website
    """
    monthly = 19
    plan = 'First Advantage'

    header = {
        'image': 'https://th.bing.com/th/id/R.00c5a689df7665ce66043a96a830dbcd?rik=bK47uc03GDr4Gw&riu=http%3a%2f%2fwww.buro247.me%2fimages%2fCA1-BK_Dining13.gif&ehk=JD6Pt2aBzXPkCFDny31UpN7IOMdioZ2xlb5vNDz1rfU%3d&risl=&pid=ImgRaw&r=0',
        'image_alt': 'People working on laptops',
        'title_first': 'Let\'s Grow Your',
        'title_second': 'restaurant revenue',
        'explainer': 'Simple plans, great pricing and a 30 day no questions money back guarantee.',
        'cta_one_url': '',
        'cta_one_label': '',
        'cta_two_url': '',
        'cta_two_label': '',
    }

    template = 'website/pricing.html'
    context = {
        'monthly': monthly,
        'plan': plan,
        'header': header,
    }
    return render(request, template, context)


def contact(request):
    """
    Show page on website
    """
    header = {
        'image': 'https://th.bing.com/th/id/R.00c5a689df7665ce66043a96a830dbcd?rik=bK47uc03GDr4Gw&riu=http%3a%2f%2fwww.buro247.me%2fimages%2fCA1-BK_Dining13.gif&ehk=JD6Pt2aBzXPkCFDny31UpN7IOMdioZ2xlb5vNDz1rfU%3d&risl=&pid=ImgRaw&r=0',
        'image_alt': 'People working on laptops',
        'title_first': 'Contact Us',
        'title_second': '',
        'explainer': 'Take control of your guest database to grow your restaurant. Powerful marketing, complete guest management and effective automated messaging that works for you.',
        'cta_one_url': '',
        'cta_one_label': '',
        'cta_two_url': '',
        'cta_two_label': '',
    }
    
    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        restaurant = request.POST['company']
        message = request.POST['message']
        message += ' ' + first_name + ' ' + last_name + ' '
        message += restaurant + ' ' + email
        send_mail('New Message', message, email, ['sean@restdos.com'])
        messages.success(request, 'You have successfully sent a message to \
                         us. We will reply to your email: {email}')

    context = {
        'header': header,
    }

    return render(request, 'website/contact.html', context)


def signup(request, signup_plan, signup_monthly):
    """
    Show page on website
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    stripe_total = round(int(signup_monthly) * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    context = {
        'signup_plan': signup_plan,
        'signup_monthly': signup_monthly,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    if not signup_plan:
        messages.error(request, 'You have not selected a signup plan')
        return redirect(reverse('pricing'))

    if request.method == 'POST':
        return redirect('account_signup')

    return render(request, 'website/signup.html', context)


def signup_success(request):
    """
    Show page on website
    """
    return render(request, 'website/new_user.html')


def terms(request):
    """
    Show page on website
    """
    header = {
        'image': 'https://th.bing.com/th/id/R.00c5a689df7665ce66043a96a830dbcd?rik=bK47uc03GDr4Gw&riu=http%3a%2f%2fwww.buro247.me%2fimages%2fCA1-BK_Dining13.gif&ehk=JD6Pt2aBzXPkCFDny31UpN7IOMdioZ2xlb5vNDz1rfU%3d&risl=&pid=ImgRaw&r=0',
        'image_alt': 'People working on laptops',
        'title_first': 'Terms & Conditions',
        'title_second': '',
        'explainer': 'Last Updated: October 18, 2021.',
        'cta_one_url': '',
        'cta_one_label': '',
        'cta_two_url': '',
        'cta_two_label': '',
    }

    context = {
        'header': header,
    }
    return render(request, 'website/terms_and_conditions.html', context)


def privacy(request):
    """
    Show page on website
    """
    header = {
        'image': 'https://th.bing.com/th/id/R.00c5a689df7665ce66043a96a830dbcd?rik=bK47uc03GDr4Gw&riu=http%3a%2f%2fwww.buro247.me%2fimages%2fCA1-BK_Dining13.gif&ehk=JD6Pt2aBzXPkCFDny31UpN7IOMdioZ2xlb5vNDz1rfU%3d&risl=&pid=ImgRaw&r=0',
        'image_alt': 'People working on laptops',
        'title_first': 'Privacy Policy',
        'title_second': '',
        'explainer': 'Last Updated: October 18, 2021.',
        'cta_one_url': '',
        'cta_one_label': '',
        'cta_two_url': '',
        'cta_two_label': '',
    }

    context = {
        'header': header,
    }
    return render(request, 'website/privacy.html', context)


def blog(request):
    """
    Show page on website
    """
    header = {
        'image': 'https://th.bing.com/th/id/R.00c5a689df7665ce66043a96a830dbcd?rik=bK47uc03GDr4Gw&riu=http%3a%2f%2fwww.buro247.me%2fimages%2fCA1-BK_Dining13.gif&ehk=JD6Pt2aBzXPkCFDny31UpN7IOMdioZ2xlb5vNDz1rfU%3d&risl=&pid=ImgRaw&r=0',
        'image_alt': 'People working on laptops',
        'title_first': 'Grow your',
        'title_second': 'restaurant revenue',
        'explainer': 'Take control of your guest database to grow your restaurant. Powerful messaging, complete guest management and effective booking management that works for you.',
        'cta_one_url': 'pricing',
        'cta_one_label': 'Get Started',
        'cta_two_url': 'live_demo',
        'cta_two_label': 'Live Demo',
    }

    context = {
        'header': header,
    }
    return render(request, 'website/blog.html', context)


def demo(request):
    """
    Show page on website
    """
    return render(request, 'website/demo.html')


def guest_crm(request):
    """
    Show page on website
    """
    return render(request, 'website/guest_crm.html')
    

def messaging(request):
    """
    Show page on website
    """
    return render(request, 'website/messaging.html')
        

def booking_management(request):
    """
    Show page on website
    """
    return render(request, 'website/booking_management.html')
    

def data(request):
    """
    Show page on website
    """
    return render(request, 'website/data.html')