from django import forms
from django.contrib.auth.forms import UserCreationForm 
from .models import User

class RegisterForm(UserCreationForm):

    full_name = forms.CharField(
        max_length=100,
        label="Full Name",
    )

    age = forms.IntegerField(
        min_value=18,
        max_value=100
    )

    email = forms.EmailField(required=True)

    role = forms.ChoiceField(
        choices=User.ROLE_CHOICES,
        widget=forms.RadioSelect
        # Use Select if you prefer a dropdown
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

    
