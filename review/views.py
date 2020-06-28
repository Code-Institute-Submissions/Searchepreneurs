from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review
from django.contrib.auth.models import User
from services.models import Service
from services.views import services


# Views for the 'review' app


def reviews(request):
    """Render the 'reviews' page."""
    return render(request, "reviews.html")


def write_review(request, id):
    """Render a form where a user can submit a review."""
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        user = User.objects.get(email=request.user.email)
        service = Service.objects.get(id=id)

        if review_form.is_valid():
            print("REVIEW FORM IS VALID")
            review = review_form.save(commit=False)
            review.review_username = user.username
            review.review_service = service.name
            review.save()
            return redirect('reviews')
    else:
        review_form = ReviewForm()
        return render(request,
                      "review_form.html",
                      {"review_form": review_form})
