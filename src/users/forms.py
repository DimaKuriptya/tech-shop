from enum import unique
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User


class LoginForm(AuthenticationForm):
    class Meta:
        model = User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2']


class UpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['image', 'first_name', 'last_name', 'email', 'phone_number']
