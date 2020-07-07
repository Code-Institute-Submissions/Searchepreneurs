# Testing

This file contains the information relevant to testing the features of this project, to ensure 
that it works as required.

## Automated Testing



## Manual Testing

### The project on different screen sizes

In terms of function, this project does not change relative to the browser or screen that it is viewd on.  

Em is used, instead of pixels, for better scalability on different screen sizes. In addition, bootstrap columns are 
utilised, so that the project's layout can remain constant on different screen sizes.  

Finally, on mobiles and tablets, the container for the index.html's title spans 80% the width of the screen, instead 
of 60%. In addition, the font-size of the title's \<h1> element is 4.1em and 2.2em on tablets and mobiles, respectively, 
compared to 5em on desktop screens.  

### Manually testing the 'authentication' feature

In order to test the authentication features manually, I went through this process:
* Register a new user
* Logout this user
* Login the user again
* Ensure the profile page information was accurate

First, I registered a new user by providing a username, email address and password in the 'registration' page, and 
verified that a new user had been created by checking that I had been redirected to the 'profile' page.  

Upon success, I clicked the 'logout' button, and verified that the navbar's contents did not contain the 'logout' or 
'profile' links.  

I then clicked on the 'login' link in the navbar, and filled in the correct information for the user, and verified 
that I was taken to the 'profile' page.  

Finally, I verified that the information on the 'profile' page (the username and email), was the same information as 
the current user.

### Manually testing the 'purchase' feature

In order to test the 'purchase' feature manually, I went through this process:
* Navigate to the 'plans' page
* Click on the 'start now' link under a plan
* Verify that I am taken to the 'purchase' page
* Fill in the form on the 'purchase' page and submit the form
* Verify that I am taken to the 'create client' page
* Fill in the form on the 'create client' page and submit the form
* Verify that a client model is generated (through the admin backend)
* Verify that, upon form submission, I am taken to the 'profile' page, and the 
client model shows up in a list on the page

First off, I clicked the 'plans' link in the navbar, and was taken to the 'services' page. I then 
chose a service, and clicked on the 'Start Now' button on the 'basic' service.  

I was then redirected to the 'purchase' page, where I filled in purchase information (I used 
Stripe's 'test' card, with a card number of 4242424242424242 and a CVV of 111).  

Upon clicking the 'submit payment' button, I was taken to the 'create_client' page, where I 
filled in the 'client' form by providing a short description, a url (I used wikipedia's homepage 
URL) and an email (I used example@email.com).  

I then clicked the 'submit client information' button, and was taken to the 'profile' page, where 
there was a single bullet point, stating "Basic purchased on July 5, 2020. Write a review."  

In addition, through the 'admin' Django backend, I manually checked the 'Clients' models for 
a model with an email of 'example@email.com' and an url of 'https://www.wikipedia.org/'.  

### Manually testing the 'review' feature

In order to test the 'review' feature manually, I went through this process:
* Purchase a plan and create a client
* Verify that there is a link next to the client on my 'profile' page with the text 'Write a 
review.'
* Click on the 'Write a review' link and verify that I am taken to the 'review form' page
* Fill in the review form (with an image), and submit the form
* Verify that I am taken to the 'reviews' page, and that my review shows up on the page

To begin, I made a purchase (using Stripe's test card number) and created a client.  

After the client model was generated, the client model's information showed up on my profile 
page, as expected, with a link to the 'review form' page.  

I clicked the link (with the text of 'Write a review.'), and was taken to the 'review_form.html' 
page. I filled in the form, providing a title, rating, description and an image. I then submitted 
the form.  

I was taken to the 'reviews' page, and my review showed up, rendered on the page, with the correct 
title, description, rating and image, as well as the correct information about when the review 
was written.

## A bug in the project - creating 'Client' models:

To purchase an audit, a user must first fill out a 'purchase' and 'payment' form, containing payment 
information, as well as additional information, such as the purchaser's first name.  

After this form is sent (and checked for validity), the user is taken to the 'create_client.html' page.  

On this page, the user can provide the URL of the site they wish to be audited, as well as an email address 
(if they wish to use one other than their account's email address), and any additional information they wish 
to provide.  

Upon submission of the 'create_client' form, a 'Client' object is generated, with the fields of:
* User (containing the user's information)
* Service (containing the information about the service they purchased)
* Purchase (containing their purchase information)
* Client Email (containing the email they provided)
* Client Description (containing the additional information they provided)
* Client URL (containing the URL of the site they wish to be audited)
* Client Date (containing the date that the Client object is generated)
* Audit Done (a boolean field, with a default of False, which shows if the audit has been completed)
* Review Done (a boolean field, with a default of False, which shows if a review for the audit has been written)

Upon creating the relevant views, models, forms and templates for this functionality, however, I ran into a 
bug, whereby a user could only ever purchase one plan from the site.  

Upon attempting to purchase a second plan from the site (as the same user), an error message would appear, stating:  

**Client object returned more than one purchase**  

By using print statements to print the session's 'user', 'purchase' and 'service', as well as manually reviewing my 
code, I found that, when a Client was being created, it was searching the 'purchases' database for a purchase model 
with the same username registered to it as the current user with this function:  

**purchase = Purchase.objects.get(username=request.purchase.username)**

For example, for a user of 'example-user', purchasing the 'basic' plan, the function would go like this:
* 'example-user' purchases the 'basic' plan by clicking the plan's button and is taken to the 'purchase' page.
* The user fills in the payment information, submits it and is taken to the 'create_client' page.
* The user fills in the client information and submits it
* The create_client view attempts to generate a 'Client' object, by querying the 'purchase' database for a 
purchase object where purchase.username = user.username

If there is only one purchase object with the user's username, then this function runs fine, however if the user 
has made more than one purchase, there will be multiple purchase objects, all of which have the same username.  

To fix this, I needed to return 'purchase' objects based off of a *unique* field. I did this by returning 'purchase' 
objects based off of their 'id' field.  

I added a hidden input to the 'create_client' form, containing the value of the relevant purchase's 'id', using the 
following code:  

**\<input type="hidden" name="purchase_id" value="{{ purchase.id }}">**

Then, in my 'views.py' file, in order to get the 'purchase' object, I used the following code:  

**purchase_id = int(request.POST.get('purchase_id'))**  

**purchase = Purchase.objects.get(id=purchase_id)**  

This allowed me to get the 'purchase' object via its 'id' field, instead of its 'username' field, meaning that a 
user could now create multiple client models.  