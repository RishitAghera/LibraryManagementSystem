from django.shortcuts import render

# Create your views here.
from django.views import generic

from book.models import Book


class AllBookList(generic.ListView):
    template_name = 'book/booklist.html'
    paginate_by = 3

    def get_queryset(self):
        return Book.objects.all()
