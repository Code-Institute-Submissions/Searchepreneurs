from django.shortcuts import render
from .models import Service


# Views for the 'services' app


def services(request):
    all_services = Service.objects.all()
    return render(request, "services.html", {"services": all_services})
