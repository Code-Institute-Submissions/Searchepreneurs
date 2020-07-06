[![Build Status](https://travis-ci.com/Felix-Redwood/Searchepreneurs.svg?branch=master)](https://travis-ci.com/Felix-Redwood/Searchepreneurs)

# Searchepreneurs

Searchepreneurs is a website that allows users to purchase 'SEO audits'. What this means is that, 
after an audit is purchased, an auditor will look through the user's site, as well as use a variety 
of programs (such as load-time checkers) to evaluate how good that site is at search engine 
optimization (SEO).

An auditor will then be able to write a report to the client, informing them of what they need to 
do to optimize their site for search engines. With higher-price audits, the auditor may also take 
their own steps (with the client's permission) to optimize the site, such as generating and 
submitting an XML sitemap.

Searchepreneurs is run off of the Django framework, to allow for authorization, template usage and 
the frictionless creation of url routes, models, templates and functions.

## UX:
---

This website is designed for business owners, where part or all of there business is online. These 
business owners want to improve their site's ranking on search engines such as google.

Searchepreneurs facilitates this, by allowing a user to purchase an 'audit' for their business's 
website. When an audit is purchased, a Searchepreneurs employee will inspect the user's site (both 
visually *and* in google devtools), as well as run it through a website speed tester such as this 
one from [dotcom tools](https://www.dotcom-tools.com/website-speed-test.aspx).

The navbar and footer of the site are a light blue, while the background for the site is white. This 
is to ensure that the site looks professional and has a consistent colour scheme.

In addition, there are four pages on the site relevant to a user's account. These are:
* The 'profile' page
* The 'login' page
* The 'password-reset' page
* The 'register' page

There is also the 'logout' function, which logs a user out.

For simplitity and minimalism, the 'profile' and 'logout' navbar links are only availible if the user 
is already logged in, while the 'login' and 'register' navbar links are only available if the user is 
*not* logged in.

In addition, the 'password-reset' page is only accesible by a link in the 'login' page, as it is 
unlikely that a user would want to reset their password before attempting to log into the site, and 
therefore it is unnecesary to have the link in the navbar.

### User Stories:

#### User Type 1 - Small business owner

* As a small business owner, I want a cheap audit that tells me the basics of what I need to do. I 
don't have a lot of resources, so I want to be given simple ways to optimize my site.

#### User Type 2 - Moderately Large Business owner

* As a moderate business owner, I want a moderately priced audit that will give me ways to optimize 
the site that are within my capabilities. I probably have the basics already optimized for the site 
and so I wish to learn new, less simple ways to optimize.

#### User Type 3 - Large Business owner

* As a large business owner, I am not sensitive to the price of the audit. I want an extensive audit 
that will thoroughly evaluate my site and will provide me with a large number of ways to optimize, 
regardless of their cost.

#### User Type 4 - Mobile User

* As a mobile user, I want to be able to access this site and pay for an audit using my mobile, as well 
as wanting the site to look good on a mobile device, so that I can browse the site and decide on a 
purchase using a mobile phone.

#### User Type 5 - Tablet User

* As a tablet user, I want to be able to access this site and pay for an audit using a tablet, as well 
as wanting the site to look good on a tablet so that I can browse the site and decide on a purchase using 
my tablet.

## Features:
---

### Feature 1 - Authentication/authorization

Feature 1 is useful to all users, as well as the site owner.  

Having access to an account and profile is useful to users, as it 
provides them a profile in which they can see what plans they have 
previously paid for (and when), allowing them to see when an audit 
may be done (within 2 business days of payment).

For the site owner, having registered users allows users' accounts 
to be linked to their purchases and their 'client' models (the 
model that contains the relevant information for the auditor).  

This allows the site owner to see which users have paid for an 
audit as well as other information such as:
* Which audit plan the user has paid for
* How many audits the user has purchased  

This information is important for functionalities such as:
* Allowing a user to write a review of an audit plan
* Verifying user complaints (e.g: checking that a user's claim 
that their audit wasn't done on time is correct)
* Implementing loyalty discouts (potential future feature)

#### Creating an account

Creating an account is important for *all* users who wish to 
purchase an audit plan.  

A user can create an account by clicking the 'register' button 
in the navbar. They then must input their email (which must be 
unique) and a chosen username (which must be unique), as well as 
a password (which must be typed twice).  

After this is done, the username and email are checked for both 
validity AND uniqueness, and then the password fields are checked 
to ensure they are the same and they are valid, and the user's 
account is registered.  

Finally, the user is redirected to their account profile.

#### Logging into an account

Being able to log into an account is invaluable for a user, as 
without login funtionality, a user would have to create a new 
account every time they wanted to purchase an audit.

A user can login by clicking the 'login' button in the navbar. 
They then must input their password as well as their email OR 
username.

After this is done, their username/email and password are 
compared against those in the database, and they and logged in 
and redirected to their account profile.

#### Viewing a user profile

A user needs to view their profile for a variety of reasons, 
such as:
* Checking their account details (email address/username)
* Checking what plans they have purchased
* Checking *when* they purchased said plans (for the 
purposes of estimating when an audit will be done)

For a user, viewing their profile is simple. All they have 
to do is click on the 'profile' link in the navbar (only 
available if they are logged in), and they are taken to their 
profile.

#### Logging out of an account

While not as neccesary as the above features, a logout 
mechanism is still a requirement for any site that employs 
authentication and authorization.  

A user may wish to logout for a variety of reasons, such as:
* Logging out to allow another user to log in on the same 
device
* Logging out on an unsecured device, whereby if the user 
remained logged in, their account could be compromised
* For curious users, logging out in order to see how the 
site looks when the user is logged out

A user can logout simply by clicking the 'logout' link on 
the navbar (only available if the user is logged in), and 
they are logged out and redirected to the homepage.

#### Resetting a password via email

Without this feature, if a user forgets their password, 
they are permanently unable to access their account.

The password-reset feature allows a user who has forgotten 
their password to enter their email into a form. Upon 
submission of the form, the user will be sent an email 
containing a link to a form allowing a user to create 
a new password.

### Feature 2 - Purchasing an audit plan

Feature 2 is useful to users of type 1, 2 and 3. These users 
have come to the site for the purposes of purchasing an SEO 
audit. There are several features that are required here:
* The ability to choose a plan
* The ability to purchase that plan
* The ability to add data specific to the client (e.g: their 
site's URL)
* Confirmation of a purchase

#### Choosing a plan

Before a user makes a purchase, they must choose a plan that 
they intend to buy. The 'services.html' page displays the 
different plans that a user can purchase.  

Each plan displays a short description, a price, and three 
basic features.  

Upon clicking the button below a plan, the user is taken to 
the 'purchase.html' page.

#### Purchasing a plan

In the 'purchase.html' page, a user is presented with a 
payment form. This form the fields of:
* credit_card_number
* cvv
* expiry_month
* expiry_year
* full_name
* phone_number
* country
* region

This form is actually a combination of the PurchaseForm and 
PaymentForm classes, with credit_card_number, cvv and the 
exipry dates coming from the PaymentForm.  

The user can input the relevant information into the form. 
Upon clicking the 'submit' button, the user is either taken 
to the 'create_client' page (if the form is valid) or redirected 
back to the 'purchase' page if the form is not valid.  

If the form is invalid, the form's errors will show up on the page.

#### Adding additional client data

For a client to be added, a user must submit the URL of their site, 
as well as provide additional information that may be useful.

When a user purchases a plan, they are redirected to the create_client 
page, where they can provide this data. After it is provided, the data 
is saved in a 'client' model, which contains all relevant information.

#### Confirmation of a purchase

Finally, it is good practice to provide the user with a confirmation 
whenever a form is filled or a model is generated. Upon the generation 
of client data, the user is sent an email, confirming their purchase 
and stating that they will be contacted by an auditor within a few 
hours.

### Feature 3 - Reviewing an audit

Feature 3 is most useful to new users of type 1 and 2, who have not yet 
purchased a plan.  

By being able to see the reviews for each audit plan, a new user can both 
evaluate the quality of each plan (based on the experiences of previous 
customers) *and* decide which plan is best for them.  

For example, a user may choose to purchase a higher-cost plan, after 
reading in a review that the higher-cost plan provides them with more 
options.  

This feature is less useful to type 3 users, as they are less cost-sensitive 
and are therefore likely to purchase the most expensive plan from the 
moment they create an account.

#### Providing a link to a review form

When a user purchases an audit, they are redirected to their profile page. On 
this page, a list of the audits that they have purchased is displayed.  

This is a list of the 'Client' models associated with the user.  

A Client model has a 'review_done' field, which is a boolean field and is 'False' 
by default.  

The list of Client models on the user's profile page will display links to the 
review_form.html page if they have not already been reviewed by the user. A user 
can click the link and can provide a title, rating, description and image for 
their review.  

Upon submitting a valid review form, the review is saved, and the 'review_done' 
field on the associated Client model is changed from 'False' to 'True'. This way, 
a user cannot submit multiple reviews for one purchase, nor can they submit a review 
without having generated a client model.

#### Displaying reviews

Reviews for audits are displayed on the 'reviews.html' page. On each review, the 
review_image (if one has been provided), rating, title, description and date_created 
are shown, so that a user is aware of what product is being reviewed.

### Features left to implement

* Ability to delete an account
* Ability to change the email/username associated with an account
* Ability to edit a review

## Technologies Used:
---

* [Bootstrap](https://getbootstrap.com/) was used for HTML, CSS and JavaScript classes.
* [Chart.js](https://www.chartjs.org/) was used to render the SEO load time chart on the homepage.
* [jQuery](https://jquery.com/) was used to simplify DOM manipulation via referencing HTML element IDs.
* [Django](https://www.djangoproject.com/) was used as a framework for the project.
* [Canva](https://www.canva.com/) was used to create the favicon and the navbar logo.
* [Font Awesome](https://fontawesome.com/) was used to display the copyright icon in the footer.
* [FreeImages](https://www.freeimages.com/) was used to get the carousel images for the homepage.
* [Heroku](https://www.heroku.com) was used to host the deployed site.
* [Github](https://github.com/) was used to store the site's code in a repository.
* [Travis](https://travis-ci.org/) was used to test the site's code.

## Testing:
---

The 'testing' section of this README is very long. As such, it has been written in a seperate markdown 
file in this project, called 'Testing.md'. That file can be found within the project files or with 
[*this link*]().

## Deployment:
---

### Setting up the ENV.PY file:

There are several variables in this project that are stored as 'environment variables'. On a platform like Heroku, 
the environment variables are stored within the app that contains the project.  

In the development version, however, these environment variables must be stored within an env.py file.  

Within the 'settings.py' file, there is this function:

import os
from os import path
if os.path.exists("env.py"):
    import env

This function first searches for the 'env.py' file. If the file is present, then this function imports the file and 
with it, the environment variables.

The env.py file is stored within the .gitignore file, as some of the variables within could create a security risk if 
they are accesible by public users. Such variables include the Stripe secret key and the Django secret key.

### Setting up Config Vars in Heroku

In Heroku (Where the deployed version of this project is hosted), there are a number of 'Config Vars' (Short for 
'configuration variables'). These are:
* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY
* DATABASE_URL
* DISABLE_COLLECTSTATIC
* SECRET_KEY
* STRIPE_PUBLISHABLE
* STRIPE_SECRET

### Setting up Travis ci

This project uses the Travis ci to test its builds. To set up Travis, I first connected the github 
repository for this project to Travis, and pasted a markdown link into the top of this README.  

Then, I created a .travis.yml file, containing the following information:  

language: python  
python:  
- "3.4"  
install: "pip3 install -r requirements.txt"  
script:  
- SECRET_KEY="secret" ./manage.py test  

This file tells Travis the language used for the project and its version, as well as providing 
an install route for the neccesary requirements and generating a placeholder SECRET_KEY variable.

### Setting up AWS S3 buckets

This project uses AWS S3 in order to host media files (such as images).  

Media files are stored in a public-access bucket called 'searchepreneurs'.  

In order to access this bucket, I have set up a group, called 'searchepreneurs' on AWS IAM 
(Identity and Access Management), with a user called 'searchepreneurs-user', and a policy 
called 'searchepreneurs-policy' that allows the group to edit the AWS S3 bucket.  

### Project Info

This project can be viewed in its rendered form (the deployed version) in Heroku [here](https://searchepreneurs.herokuapp.com/). 
It can also be viewed in its code form (the development version) in Github
[here](https://github.com/Felix-Redwood/Searchepreneurs).

In the development version of this project, environment variables are stored in an env.py file, and DEBUG is set 
to True. In the deployed version, environment variables are stored in Heroku, and DEBUG is set to False.

#### Running the Code Locally

To run this code locally, you must first open this project, either in Gitpod, or another IDE of your choice.  

After this, use the command:

__pip3 install -r requirements.txt__  

This will install the requirements for the project on your IDE.  

## Credits:
---

### Content:

* [Bootstrap](https://getbootstrap.com/) was used for its prewritten CSS stylings and JavaScript objects.

### Media:

* Media for this site was taken from [FreeImages](https://www.freeimages.com/).

### Acknowledgements:
* Privacy Policy template was taken from [TermsFeed](https://www.termsfeed.com/blog/sample-privacy-policy-template/#Download_Privacy_Policy_Template)

* I gained the coding knowledge neccesary to make this site from the [Code Institute](https://codeinstitute.net/), Dublin.
* [StackOverflow](https://stackoverflow.com/) and [w3schools](https://www.w3schools.com/) were also useful resources during the creation of this project.