from django.contrib import admin
from .models import Purchase, Client


# Admin for the 'checkout' app, where models are registered


class ClientAdminInline(admin.TabularInline):
    model = Client


class ClientAdmin(admin.ModelAdmin):
    inlines = (ClientAdminInline, )


admin.site.register(Purchase, Client)
