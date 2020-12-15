from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect
from users.forms import LoginForm

# Create your views here.
from django.views import View

from users.forms import RegistrationForm

from users.forms import LoginForm

from LMS import settings

from django.views import generic

from .models import User

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


class Login(View):
    def get(self, request):
        form = LoginForm()
        # messages.warning(request, 'Please Login in order to continue!')
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            # if user is not None:
            #     if user.is_staff:
            #         login(request, user)
            #         return redirect('book:approval')
            #     login(request, user)
            #     return redirect('book:booksearch')
            # else:
            #     messages.error(request, 'User Not Found please Enter Valid data' + str(form.errors))
            if user:
                login(request, user)
                print('authenticated')
                return redirect('index')
            else:
                print(' not authenticated')
                form = LoginForm()
                return render(request, 'users/login.html', {'form': form})

def Logout(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)


class ProfileView(generic.DetailView):
    model = User
    template_name = 'users/profile.html'
    extra_context = {'form': RegistrationForm()}

class ProfileUpdate(generic.UpdateView):
    model = User
    fields = ['name', 'username', 'gender', 'contact']
