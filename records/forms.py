from django import forms
from django.contrib.auth.forms import UserCreationForm,UsernameField
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
    max_length=200,
    required = True,
   
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    )
    password1 = forms.CharField(
    required = True,
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
    required = True,
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),
    )
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']