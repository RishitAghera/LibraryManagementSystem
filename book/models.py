from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50,null=True)
    information = models.CharField(max_length=200)
    total_stock = models.PositiveIntegerField(default=0)
    avail_stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '(' + str(self.category) + ') ' + str(self.name)
