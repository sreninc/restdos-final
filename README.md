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


# RestDos
[Click To See Live Site](https://restdos-final.herokuapp.com/)

RestDos is an app and website designed to help owners of small restaurants manage their guests, bookings and messaging. It acts as a complete CRM that empowers the restaurant team to deliver perfect service each and every time. 

[![RestDos]()](https://restdos-final.herokuapp.com/)

## CONTENTS
1. [User Stories](#user-stories)
1. [Design and UX](#design-and-ux)
    - Mockups
1. [Website Pages and Features](#website-pages-and-features)
    - Common Features
    - Hompage
    - Solutions
    - Contact
    - Pricing
    - Blog
    - Live Demo
    - Privacy
    - Terms
    - Newsletter Signup
    - Signup
    - Confirm Email
    - Confirmed confirm Email
    - Login

1. [App Pages and Features](#app-pages-and-features)
    - Common Features
    - Dashboard
    - Guests
        - Add Guest
        - Guest Detail
        - Delete Guest
    - Bookings
        - Add Bookings
        - Edit Booking
        - Delete Booking
    - Messaging
        - Compose Message
        - Pay & Send Message
    - Help
    - Logout
1. [Database Schema](#database-schema)
1. [Testing](#testing)
1. [Bug and Issues Log](#bug-and-issues-log)
1. [Potential Future Features](#potential-future-features)
1. [Deployment](#deployment)
    - [GitHub Pages](#github-pages)
    - [Forking the GitHub Repository](#forking-the-github-repository)
    - [Making a Local Clone](#making-a-local-clone)
    - [Tailwind](#Tailwind)
    - [Heroku](#Heroku)
    - [AWS](#AWS)
1. [Credits & Attribution](#credits-and-attributions)

***

## Project Stories

### User Stories
As a user I want to ...
- Signup
- CRUD Guests
- CRUD Bookings
- Send messages to my guests

### Business Stories
As the website owner I want to ...
- Drive signups
- To receive money from signups
- Be able to manage queries from users
- Be able to help users with queries or changes to their accounts

***

## Design and UX


### Website Mockups
The below image links to figma design file of website side the application.
[![Website]()](https://www.figma.com/file/qAy7XQsKaKW6ekC1ssgalx/MS4?node-id=0%3A1)

The below image links to figma design file of app side the application.
[![App]()](https://www.figma.com/file/qAy7XQsKaKW6ekC1ssgalx/MS4?node-id=6%3A1470)

***

## Website Pages and Features

### Common Features

### Homepage


### Solutions

### Contact

### Pricing

### Blog

### Live Demo

### Privacy

### Terms

### Newsletter Signup

### Signup

### Confirm Email

### Confirm confirmed Email

### Login

## App Pages and Features

### Common Features
1. Login is required on all pages. Users accessing the urls directly will be directed to the login page for authentication.
1. There is a global guest search at the top of each page. Users can search for guests by name, mobile or email. They will see different things based on the results of their search:
- No Results: Empty guests page with notification that their search returned no results
- 1 Result: The guest detail page for the guest.
- 2+ Results: The guest page filtered to show these guests as well as a notification to say how many guests were returned.

### Dashboard
This page shows some key statistics about the salons performance on RestDos. It shows figures for their entire time with RestDos.
- Total Guests: The count of guest profiles not deleted.
- Total Bookings: The total number of bookings not deleted.
- Total Sales: The sum of booking value for bookings marked completed.
- % No-Shows: The number of bookings with status no-show that are not deleted divided by the total number of bookings that are not deleted.
- % Completed: The number of bookings with status completed that are not deleted divided by the total number of bookings that are not deleted.
- Avg. Booking Value: Total Sales divided by the number of bookings with status completed that are not deleted.

### Guests
This page shows a table of guests information. They can also add a guest for here

#### Add Guest

#### Guest Detail

#### Delete Guest

### Bookings

#### Add Bookings

#### Edit Booking

#### Delete Booking

### Messaging

#### Compose Message

#### Pay & Send Message

### Help

### Logout


***

## Database Schema

### Guests

### Bookings

### Signup

### Messaging

***

## Testing

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

***

## Bugs and Issues Log

***

## Potential Future Features
1. Reports
1. Transactional Messaging
1. Users
1. Booking Widget

***

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/sreninc/financial-freedom)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://sreninc.github.io/financial-freedom/) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/sreninc/financial-dreedom)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/sreninc/financial-freedom)
2. Under the repository name, click the "Code" button and a dropdown menu will appear.
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

8. Tailwind
9. Heroku
10. AWS S3

***

## Credits and Attributions
1. Tailwind
1. Stackoverflow
1. Heroicons
1. Djangoproject