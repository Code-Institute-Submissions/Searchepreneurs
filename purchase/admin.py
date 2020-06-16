from django.contrib import admin
from .models import Purchase, Client


# Admin for the 'purchase' app, where models are registered


class ClientAdminInline(admin.TabularInline):
    model = Client


class ClientAdmin(admin.ModelAdmin):
    inlines = (ClientAdminInline, )


admin.site.register(Purchase)
admin.site.register(Client)
