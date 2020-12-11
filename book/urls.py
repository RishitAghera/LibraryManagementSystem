from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('list/',views.AllBookList.as_view(),name='booklist'),
    path('delete/<int:pk>/',views.BookDelete.as_view(),name='bookdelete'),
]