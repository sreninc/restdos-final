# restdos-final

Deployment
1. pip3 install -r requirements.txt
1. python3 manage.py tailwind install
1. python3 manage.py tailwind start
1. python3 manage.py migrate
1. python3 manage.py createsuperuser
1. python3 manage.py loaddata guests
1. python3 manage.py loaddata signups
1. python3 manage.py runserver



# Testing

## Website
- Email signup works
### Homepage
- Links work
- Content appears right on mobile, tablet and desktop
- Colour scheme is consistent
- Lighthouse, pep8
- no lorem ipsum
### Solutions
### Pricing
- Correct pricing appears
### Blog
### Contact
- Send message works properly
- Loading icon works properly
- Form validation functions
### Live Demo
- Video plays as expected
### Privacy
### Terms
### Login
- Correct login directs to dashboard
- Incorrect details informs user of error
- Form validation functions correctly
### Forgot Password
- Email functions correctly
### Signup
- Existing email won't allow signup
- Form validation works
- Stripe payment successfully taken
- Error if card details wrong
- Loading symbol functions correctly
### Confirm Email
- email sends correctly
- should not be able to access directly outside of email link
### Confirm confirmed Email
- When confirmed user is directed to help page
- should not be able to access directly

## App
### Dashboard
### Guests
1. Guests
1. Add Guest
1. Guest Detail
### Bookings
1. Bookings
1. Add Booking
1. Edit Booking
### Messaging
1. Compose Message
1. Send Message
### Help
### Signout Confirmation