from django.shortcuts import render, redirect, reverse
from .forms import ReviewForm
from .models import Review
from django.contrib.auth.models import User
from purchase.models import Client
from services.models import Service
from services.views import services


# Views for the 'review' app


def reviews(request):
    """Render the 'reviews' page."""
    reviews = Review.objects.all()
    return render(request, "reviews.html", {'reviews': reviews})


def write_review(request, id):
    """Render a form where a user can submit a review."""
    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES)
        print(review_form)
        user = User.objects.get(email=request.user.email)
        client = Client.objects.get(id=id)
        print(client)

        if review_form.is_valid():
            print("REVIEW FORM IS VALID")
            review = review_form.save(commit=False)
            review.review_username = user.username
            review.review_service = client.service.name
            review.save()
            client.review_done = True
            client.save()
            return redirect('reviews')

        else:
            print("INVALID REVIEW FORM")
            print(review_form.errors)
    else:
        review_form = ReviewForm()
        client = Client.objects.get(id=id)
        return render(request,
                      "review_form.html",
                      {"review_form": review_form,
                       "client": client})
