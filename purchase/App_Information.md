# Purchase


## App description:

This is the purchase app. This app will be used to allow the user to 
purchase a service.


## App purpose:

The primary purpose of this app is to render a payment form, where the 
user can input their payment data and purchase a service.

This app will also allow a user to provide the URL of the site that they 
want audited, an optional alternate email to be contacted via (if they 
do not wish to use the email they signed up with) and an additional 
information for the auditor.

Finally, upon purchase, a one-time token will be generated, which will 
be used in the 'review' app. By generating one token per purchase, it 
is ensured that nobody can write a review without purchasing an audit 
and nobody can write multiple reviews for one audit.


# App contents:

This app will contain the templates, views, forms and urls 
relevant to:
* Providing financial data necessary to purchase a service
* Rendering the form in which financial data is provided
* Rendering the form in which additional data (such as the user's 
site's URL) is provided

In addition, this app will contain a 'tokens.py' file, which will 
generate a one time token upon purchase of a product.
