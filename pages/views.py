from django.shortcuts import render


# Views for the 'pages' app.


def index(request):
    """Renders the index.html page"""
    return render(request, "index.html")
