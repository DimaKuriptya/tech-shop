from django import forms
from .models import User


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=150, label='Логін', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=150, label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password')
