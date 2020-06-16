# Review


## App description:

This is the review app. This will allow a user to write AND edit a 
review each time they purchase a service.


## App purpose:

The purpose of this app is to use CRUD (Create, Read, Update, 
Delete) functions to allow users to write and edit reviews.

Reviews will be rendered in html for new users to see, while 
a user that has purchased a service will be able to generate 
a review using a one time token, generated upon purchase.

A user will also be able to edit their review, as well as 
delete it, if they wish to.


# App contents:

This app will contain the templates, views, models, forms 
and urls relevant to:
* Creating a new review
* Ensuring that only one review can be created per purchase
* Editing an existing review
* Deleting a review
* Rendering reviews in html
* Ensuring that the only user able to edit or delete a review 
is the one who created the review in the first place
