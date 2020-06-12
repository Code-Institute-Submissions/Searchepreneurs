from django.conf.urls import url, include
from .views import services


# Urls for the 'services' app


urlpatterns = [
    url(r'^$', services, name="services"),
]
