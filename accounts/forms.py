from django import forms


# Forms for the 'accounts' app


class UserLoginForm(forms.Form):
    """Form used to log users in."""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
