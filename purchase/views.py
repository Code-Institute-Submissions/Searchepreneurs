from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from .forms import PurchaseForm, PaymentForm, ClientForm
from .models import Purchase
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.utils import timezone
from services.models import Service
from services.views import services
import stripe


# Views for the 'checkout' app


stripe.api_key = settings.STRIPE_SECRET


@login_required
def purchase(request):
    if request.method == "POST":
        purchase_form = PurchaseForm(request.POST)
        payment_form = PaymentForm(request.POST)
        user = User.objects.get(email=request.user.email)
        service = Service.objects.get(name=request.service.name)

        if payment_form.is_valid() and purchase_form.is_valid():
            purchase = purchase_form.save(commit=False)
            purchase.date = timezone.now()
            purchase.username = user.username
            purchase.save
            price = service.price

            try:
                customer = stripe.Charge.create(
                    amount = int(price * 100),
                    currency = "GBP",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card has been declined")

            if customer.paid:
                messages.success(request, "You have succesfully paid")
                return render(request,
                              "create_client.html",
                              {"purchase": purchase, "service": service, "user": user})
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "Payment cannot be taken with that card")
    else:
        purchase_form = PurchaseForm()
        payment_form = PaymentForm()
    return render(request,
                  "purchase.html",
                  {"purchase_form": purchase_form},
                  {"payment_form": payment_form})


@login_required
def create_client(request):
    if request.method == "POST":
        client_form = ClientForm(request.POST)
        user = User.objects.get(email=request.user.email)
        service = Service.objects.get(name=request.service.name)
        purchase = Purchase.objects.get(username=request.purchase.username)

        if purchase:
            if client_form.is_valid:
                client = client_form.save(commit=False)
                client.user = user
                client.service = service
                client.purchase = purchase
                client.client_date = timezone.now()
                client.save
                messages.success(request, "Thank you for purchasing an audit! We will be in touch shortly")
                send_mail(
                    "You recently purchased a site audit",
                    str("Hello " + user.username + "\n" + "\n" + "You recently purchased an audit with Searchepreneurs. One of our auditors will send you an email shortly to introduce themselves to you. Your site is being audited as we speak."),
                    "admin@example.com",
                    [str(user.email)],
                    fail_silently=True,
                )
                return redirect('profile')
            else:
                print(client_form.errors)
                messages.error(request, "Form is invalid")
        else:
            return redirect(reverse('purchase'))

    else:
        client_form = ClientForm()
        user = User.objects.get(email=request.user.email)
        service = Service.objects.get(name=request.service.name)
        purchase = Purchase.objects.get(date=request.purchase.date)
    return render(request, "create_client.html",
                  {"purchase": purchase, "service": service, "user": user})


def redirect_to_services(request):
    return redirect(reverse('services'))
