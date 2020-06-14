from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm


# Views for the 'accounts' app.


def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have logged in to your account")
                return redirect('profile')
            else:
                login_form.add_error(None,
                                     "Your username, email or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, "login.html", {'login_form': login_form})


def register(request):
    """Render the register.html page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have succesfully registered")
                send_mail(
                    "Your account has been registered",
                    str("Hi " + user.username + "\n" + "\n" + "You have succesfully registered an account with Searchepreneurs. We hope to work with you soon!"),
                    "admin@example.com",
                    [str(user.email)],
                    fail_silently=True,
                )
                return redirect('profile')
            else:
                messages.error(request,
                               "Unable to register your account at this time")

    else:
        registration_form = UserRegistrationForm()

    return render(request, "register.html",
                  {"registration_form": registration_form})


@login_required
def logout(request):
    """Logs the user out of their account"""
    auth.logout(request)
    messages.success(request, "You have succesfully logged out")
    return redirect(reverse('index'))


@login_required
def profile(request):
    """Renders the user's profile"""
    user = User.objects.get(email=request.user.email)
    return render(request, "profile.html", {'profile': user})
