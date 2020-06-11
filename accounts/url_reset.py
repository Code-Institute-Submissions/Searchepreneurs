from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_complete, password_reset_confirm


# Urls for the 'accounts' app, used to reset a user's password


"""
<uidb64> is the user's ID, encoded in base 64

[0-9A-Za-z] allows the ID to be encoded using numbers 0-9, and
each character in the alphabet, in either lower or uppercase
forms
"""
urlpatterns = [
    url(r'^$',
        password_reset,
        {'post_reset_redirect': reverse_lazy('password_reset_done')},
        name="password_reset"),
    url(r'^done/$', password_reset_done, name="password_reset_done"),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm,
        {'post_reset_redirect': reverse_lazy('password_reset_complete')},
        name="password_reset_confirm"),
    url(r'^complete/',
        password_reset_complete,
        name="password_reset_complete"),
]
