from django.contrib.auth.models import User


# Backends for the 'accounts' app


class EmailAuth:
    """Authenticate a user by an exact match on the email and password"""

    def authenticate(self, username=None, password=None):
        """Get an instance of the user based off of the email, then
        verify the password"""

        try:
            """We search for a user, where the user's email address
            matches the email provided in the 'username' field"""
            user = User.objects.get(email=username)

            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """Get an instance of the user from the user_id"""

        try:
            user = User.objects.get(pk=user_id)

            if user.is_active:
                return user
            else:
                return None
        except User.DoesNotExist:
            return None
