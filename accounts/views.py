from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm


# Views for the 'accounts' app.


def logout(request):
    """Logs the user out of their account"""
    auth.logout(request)
    messages.success(request, "You have succesfully logged out")
    return redirect(reverse('index'))


def login(request):
    """Return a login page"""
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have logged in to your account")
            else:
                login_form.add_error(None,
                                     "Your username, email or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, "login.html", {'login_form': login_form})
