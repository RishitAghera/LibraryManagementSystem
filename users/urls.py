"""LMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from users.views import index

from users.views import Registration

from users.views import Login,Logout

urlpatterns = [
    path('', index, name='index'),
    path('registration/', Registration.as_view(), name='registration'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout, name='logout'),
    # path('profile/<int:pk>/', ProfileView.as_view(), name="profile"),
    # path('profile/update/<int:pk>/', ProfileUpdate.as_view(), name="update-profile"),
]

