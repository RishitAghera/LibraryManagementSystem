from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from book.models import Book


class AllBookList(generic.ListView):
    template_name = 'book/booklist.html'
    paginate_by = 3

    def get_queryset(self):
        return Book.objects.all()

class BookDelete(generic.DeleteView):
    model = Book
    success_url = reverse_lazy('book:booklist')

class BookUpdate(generic.UpdateView):
    model = Book
    fields = '__all__'

