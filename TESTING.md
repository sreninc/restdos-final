# RestDos Testing

## Website

TEST | OUTCOME | PASS/FAIL
----|----|----
All links on the website pages function and bring me to the expected page | All links in header, body and footer function as expected | PASS
All imagery loads correctly depending on screen size | All images loaded correctly and resized in a way that made sense | PASS
There is no lorem ipsum text present on the site | There was no lorem ipsum found on the site | PASS
The content itself resizes in a way that makes sense for mobile, tablets and browsers | All content changed in a way that made sense, and delivered a good UX | PASS
I was able to send a message throught the contact form and receive feedback that my message had sent | This functioned as expeceted and I received notification that the message had been sent | PASS
I can signup to the newsletter | This functioned as expected and I received a notification on screen that the email I had entered was signed up to the newsletter | PASS
The pricing on the pricing page showed correctly based on the number of current users | This functioned as expeceted with the price increasing as the number of users increased until the standard full price was in effect | PASS


## Signup / Registration Flow / Authentication

TEST | OUTCOME | PASS/FAIL
----|----|----
When entering an email address if the user already exists I should see a warning message informing me of the fact | This happened as expected | PASS
When entering a new email address I should proceed to payment | PASS
On the signup payment I shoudl see the plan name and monthly cost that I have selected | This appears as expected | PASS
When entering incorrect details in the stripe module I should see inline errors | When incorrect details where entered the section turned red to indicate to the user that there was something wrong | PASS
When clicking pay a loading modal appears to let me know something is happening | This happened as expected and the modal disappeared once the action was completed | PASS
When authentication is required a modal should appear from stripe | This functioned as expected and had the buttons to complete or decline | PASS
If authentication fails with stripe I'm brought back to the page to attempt payment again | When it failed I was shown an error message to let me know it had failed and I needed to try again. | PASS
When payment is successfull show the user | When payment was successful I was brought to the final signup page as expected | PASS
Don't allow any fields to not be completed in the final signup form | This functioned as expected and I was not allowed to signup without the information compelted | PASS
A confirmation page is shown and the user is sent an email as expected | I was taken to the page as expected and received the email | PASS
When I click the link in the email I am brought to a confirm page that when clicked redirects to the login page | This functioned as expected | PASS 
All pages should resize appropriately for mobile, tablet and desktop screens.  | Using google chrome inspect for mobile s, tablet and laptop the page resized correctly. Both pages resized all components as expected and in a pleasing manner to ensure good UX.  | PASS
When I click forgot password I can request a new password | This functioned as expected | PASS
I can complete the entire forgot password experience including receiving emails with functioning links to complete the process | This funcitoned as expected and I was able to complete the process | PASS
I am asked to confirm my intention to logout when clicking the logout button in the app | This functioned as correctly and brought me to the signin page once logout has been confirmed | PASS
When logged out I was not able to directly access any page in the application not in the website | This functioned as expected and brought me to the login page when I tried to access a login required page | PASS


## Dashboard

TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Users without data should see no figures in the dashboard cards | This is working as expected where all stats are 0 | PASS
The total guests should match the number of guests visible on the guests screen | Adding a new guest increased the count and deleting a guest decreased the count. | PASS
The total bookings should match the number of non deleted bookings created for guests | Adding a new booking increased the count and deleting a booking decreased the count. | PASS
The total sales should match the sum of booking values for all bookings with status completed | Completed bookings added to the total sales metric as expected and removing the booking, changing it's status or altering the booking value updated the metric as expected. | PASS
% No Show should equal the count of bookings with status no-show divided by the count of all bookings that are not deleted | Adding and removing bookings with status of no-show both by updating the status and deleting the booking updated the metric as expected | PASS
% Completed should equal the count of bookings with status completed divided by the count of all bookings that are not deleted | Adding and removing bookings with status of no-show both by updating the status and deleting the booking updated the metric as expected | PASS
Avg. Booking value should equal the total sales divided by the count of bookings with status completed | The metric was dividing total sales by all bookings rather than just completed bookings. A fix was deployed that fixes the issue as shown: [9f0a6f9](https://github.com/sreninc/restdos-final/commit/9f0a6f93d6f9f8ae244d2995976b63d9dcd38666) | FAIL
The dashboard tiles should resize appropriately for mobile, tablet and desktop screens | Using google chrome inspect for mobile s, tablet and laptop all tiles resized appropriately and were legible | PASS
I should be able to add a booking for a guest using the CTA at the top of the screen | Clicking the button successfully brought me to the add booking page | PASS

## Guests

TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
When no guest profiles are available the user should see an empty state message in the table | With no guests available I see a message saying no guests available | PASS
When guests are available I should see them listed in alphabetical order by first and last name. | Entering guests such as Adam Adams, Adam Lidtz and Adam Lia showed them in the expected order in the list | PASS
The guest details should appear as they are in the profile page for the guest. | Updating guest details, in particular the guest rating displayed the expected results in the guest list | PASS
The add guest button should bring me to the add guest page | Worked as expected | PASS
The guest table should resize appropriately for mobile, tablet and desktop screens | Using google chrome inspect for mobile s, tablet and laptop the page resized correctly with small screens having the ability to scroll the table left to right as needed | PASS
I shouldn't be able to create a guest without entering at least first name, last name, mobile and email | Trying to create a guest without one of these fields results in an error message appearing on the offending field | PASS
I can't create an invalid email | Trying to save a profile with a malformed email (susan@, .com@, a@.com) was no allowed | PASS
The add guest form should resize appropriately for mobile, tablet and desktop screens | Using google chrome inspect for mobile s, tablet and laptop the page resized correctly with form fields wrapping onto seperate lines to ensure a good UX | PASS
Successfully saving a new guest should bring me to the guest detail page for that guest | On saving it brought me to the right page as expected | PASS
Deleting a guest should remove them from the list, and should make them inaccessible via direct url | The guest was removed from the list successfully but was still active via direct url. A fix was deployed that fixes the issue as shown: [5e67ea4](https://github.com/sreninc/restdos-final/commit/5e67ea4e1a6c9f57036bddb6b8cc06a8fd66794d) which redirects users to a 404 page when trying to access a deleted guest | FAIL  
I should be able to update and save all guest detail fields with appropriate data (e.g. rating 1-5) | All fields functioned as expected with the exception of the rating field which allowed values outside of 1 and 5 to be inputted. A fix was deployed that fixes the issue as shown: [140c749](https://github.com/sreninc/restdos-final/commit/140c7495f1bc0458b33b82fa11f00b37be7495ed) which shows errors when values outside 1-5 are inputted | FAIL
Only active bookings should show in the bookings section of the guest details | Deleted bookings disappeared from the section and new bookings appeared as expected | PASS
The sections in guest details should resize appropriately for mobile, tablet and desktop screens | Using google chrome inspect for mobile s, tablet and laptop the page resized correctly with small screens having the ability to scroll the bookings table left to right as needed. The stats section while it did resize correctly for each screen size doesn't look as good as it could on the 1024px screen. A #potential-future-fix.  | PASS

## Bookings

TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
I should be directed to 404 when trying to direct access add booking for a deleted guest | This was not happening. A fix was deployed that fixes the issue as shown: [bf7a278](https://github.com/sreninc/restdos-final/commit/bf7a2787f3dd85912448cd7f3a2d7192f289e960) | FAIL
I should not be able to add a booking without all fields being completed | If I didn't fill in all fields the form correctly stopped me from submitting it | PASS
I should not be able to add "People" less than 1 or a guest rating outside of 1-5 | The guest rating functioned as expeceted with errors showing. The people field stopped decimal numbers but allowed negative and 0. A fix was deployed that fixes the issue as shown: [8dc23a9](https://github.com/sreninc/restdos-final/commit/8dc23a9ca0a61d307a17011243823525af2a71f5) | FAIL
Deleting a booking should remove it from the bookings tables and stop me accessing the booking directly via url | The booking when deleted removed itself from all booking lists however I was able to access it directly via URL. A fix was deployed that fixes the issue as shown: [a6b3f4d](https://github.com/sreninc/restdos-final/commit/a6b3f4d5f8218ae04261457e2bbe275ee069ac01) that redirects the user to a 404 page. | FAIL
The form in add booking should resize appropriately for mobile, tablet and desktop screens | Using google chrome inspect for mobile s, tablet and laptop the page resized correctly.  | PASS
I should be able to filter the bookings list by status and date | Changing the status showed the correct bookings and where no booking was available informed the user. Changing the date had the same effect where it showed the bookings for that date with the corresponding status. | PASS
I should be able to access the guest detail page and booking edit page for each booking in the list | This functioned as expected where I could access the right guest and right booking edit page for each item in the list | PASS
The table and filters on the bookings page should resize appropriately for mobile, tablet and desktop screens.  | Using google chrome inspect for mobile s, tablet and laptop the page resized correctly. The filters wrapped as expected on all screen sizes. The table also resized as expected including on smaller screens where the user was able to scroll the table itself left to right.  | PASS
When saving a booking that I am editing I should be taken to the bookings page for that status and date | When saving it took me to the bookings page with the expected filters. | PASS
I should not be able to have booking values less than 0 | This was not working, I was able to save negative values. A fix was deployed that fixes the issue as shown: [e3cd723](https://github.com/sreninc/restdos-final/commit/e3cd723b5d5a1c05860d96db6c7a27e407cd88d5)


## Messaging

TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
I should be able to create a message upto 459 characters long in order to precede to send | When going above 459 characters a warning message appeared informing me that I needed to reduce the characters in my message as excpted | PASS
I should be able to choose all guests filter | This is currently the only filter available | PASS
I should see a character count and sms quantity as I type my message | This appears and updates correctly when typing each letter in the message | PASS
In the send message page I shoudl see the filter I choose | This appears as expcted | PASS
In the message page the guests should match the dashboard total guests figure | It matched the figure as expected | PASS
In the message page the character count and messages being sent should match the compose sms page | The figures matched as expected | PASS
The price displayed to send the campaign should match the number of guests * the sms per guest * 8c. | This worked as expected where 10 guests * 3 SMS * 8c = €2.4 | PASS
If the price is less than stripes minimum of €1 then I should be informed of the minimum charge I am about to pay. | A warning message appeared as expected when the above calculation was less than €1. | PASS
When entering incorrect details in the stripe module I should see inline errors | When incorrect details where entered the section turned red to indicate to the user that there was something wrong | PASS
When clicking pay a loading modal appears to let me know something is happening | This happened as expected and the modal disappeared once the action was completed | PASS
When authentication is required a modal should appear from stripe | This functioned as expected and had the buttons to complete or decline | PASS
If authentication fails with stripe I'm brought back to the page to attempt payment again | When it failed I was shown an error message to let me know it had failed and I needed to try again. | PASS
When payment is successfull show the user | When payment was successful I was brought back to the messaging homepage and shown a success message to let me know the campaign was sent | PASS
The compose and send messaging pages should resize appropriately for mobile, tablet and desktop screens.  | Using google chrome inspect for mobile s, tablet and laptop the page resized correctly. Both pages resized all components as expected and in a pleasing manner to ensure good UX.  | PASS


## Help

TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
I should be able to scroll to each section by clicking on the table of contents | This functioned as expected | PASS
The content should resize appropriately for mobile, tablet and desktop screens.  | Using google chrome inspect for mobile s, tablet and laptop the page resized correctly. All components resized as expected and in a pleasing manner to ensure good UX.  | PASS