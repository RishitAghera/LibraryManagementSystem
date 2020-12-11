from django.contrib import admin

# Register your models here.
from book.models import Category, Book, Author

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Author)