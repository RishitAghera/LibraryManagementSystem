from django.contrib.auth.forms import UserCreationForm

from users.models import User


class RegistrationForm(UserCreationForm):
    # gender = forms.CharField(widget=forms.Select(choices=GENDER_CHOICE))

    class Meta:
        model = User
        fields = ('name','username','email','gender','contact', 'password1', 'password2')