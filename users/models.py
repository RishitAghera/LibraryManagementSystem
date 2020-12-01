from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
GENDER = (('M', 'Male'),
          ('F', 'Female'))


class User(AbstractUser):

    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER)
    contact = models.PositiveIntegerField(unique=True,null=True,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return str(self.name)

    # def get_absolute_url(self):
    #     return reverse('users:profile',kwargs={'pk':self.pk})