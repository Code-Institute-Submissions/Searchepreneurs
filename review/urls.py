from django.conf.urls import url
from .views import reviews, write_review


urlpatterns = [
    url(r'^$', reviews, name="reviews"),
    url(r'^write_review/(?P<id>\d+)', write_review, name="write_review"),
]
