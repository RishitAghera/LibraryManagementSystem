from django.contrib.auth.forms import UserCreationForm
from django import forms

from users.models import User


class RegistrationForm(UserCreationForm):
    # gender = forms.CharField(widget=forms.Select(choices=GENDER_CHOICE))

    class Meta:
        model = User
        fields = ('name','username','email','gender','contact', 'password1', 'password2')


class LoginForm(forms.Form):
    email = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())
