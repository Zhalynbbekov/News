from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Register(models.Model):
    first_name = models.CharField('first_name', max_length=50)
    last_name = models.CharField('last_name', max_length=50)
    user_name = models.CharField('uname', max_length=50)
    password = models.CharField('password', max_length=50)
    password_again = models.CharField('password_again', max_length=50)

    def __str__(self):
        return self.first_name


class News(models.Model):
    data = models.DateField(verbose_name='data', auto_now=True)
    title = models.CharField(max_length=50)
    paragraph = models.TextField()
    image = models.ImageField(upload_to='news/')

    def __str__(self):
        return self.title

# class Login(models.Model):
#     user_name = models.CharField('uname', max_length=50)
#     password = models.CharField('password', max_length=50)
#
#     def __str__(self):
#         return self.user_name
