from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    """
    Customizing user creation so that registration will also require
    a valid email address which is not available in the default
    UserCreationForm
    """
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]



