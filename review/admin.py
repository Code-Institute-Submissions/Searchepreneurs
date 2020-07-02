from django.contrib import admin
from .models import Review


# Admin for the 'review' app, where models are registered

admin.site.register(Review)
