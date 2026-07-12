from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):

    full_name = forms.CharField(
        max_length=100,
        label="Full Name",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your full name"}),
    )

    age = forms.IntegerField(
        min_value=18,
        max_value=100,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Enter your age"}),
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "you@example.com"}),
    )

    role = forms.ChoiceField(
        choices=User.ROLE_CHOICES,
        widget=forms.RadioSelect(attrs={"class": "role-options"}),
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Choose a username"}),
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Create a password"}),
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm password"}),
    )

    class Meta:
        model = User
        fields = [
            "full_name",
            "age",
            "email",
            "role",
            "username",
            "password1",
            "password2",
        ]

    
class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)
    