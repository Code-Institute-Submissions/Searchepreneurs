# Purchase


## App description:

This is the purchase app. This app will be used to allow the user to 
purchase a service.


## App purpose:

The primary purpose of this app is to render a payment form, where the 
user can input their payment data and purchase a service.

This app will also render a create_client form, which will, upon being 
submitted, bring together the purchase data, the user's data, 
the service's data and additional data provided by the user (client 
email, client url and client description), to create one 'Client' 
object containing this data.  

The 'Client' object will also be used in the 'review' app, as the 
Client object as a field of 'review_done' (a boolean field), which 
will be 'False' if the Client hasn't been reviewed, and 'True' if 
a review about the client has been made.

# App contents:

This app will contain the templates, views, forms and urls 
relevant to:
* Providing financial data necessary to purchase a service
* Rendering the form in which financial data is provided
* Rendering the create_client form in which additional data (such as the user's 
site's URL) is provided
* Generating a client object that incorporates user, client, purchase 
and service data
