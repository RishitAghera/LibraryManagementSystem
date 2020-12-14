from django.forms import forms
from .models import Book


class BookRegistrationForm(forms.Form):

    class Meta:
        model = Book
        fields = ('category','name','author','information')