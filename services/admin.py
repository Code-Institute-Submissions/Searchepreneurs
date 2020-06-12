from django.contrib import admin
from .models import Service


# Admin for the 'services' app, where models are registered


admin.site.register(Service)
