from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from users.forms import RegistrationForm


def index(request):
    return render(request, 'users/index.html')


class Registration(View):

    def get(self, request):
        form = RegistrationForm()
        return render(request, 'users/registrations.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            # messages.error(request, 'Registration fail..')
            return render(request, 'users/registrations.html', {'form': form})
        return redirect('index')
        # messages.info(request, 'Registration successfully..')
