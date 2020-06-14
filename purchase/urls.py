from django.conf.urls import url
from .views import purchase, create_client, redirect_to_services


urlpatterns = [
    url(r'^$', redirect_to_services, name="redirect_to_services"),
    url(r'^purchase/(?P<id>\d+)', purchase, name="purchase"),
    url(r'^create_client/(?P<id>\d+)', create_client, name="create_client"),
]
