from django.db import models
from django.utils import timezone



# Create your models here.
class logmodel(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username

class book(models.Model):
    bookname = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    pdf = models.FileField(upload_to='bookmanagmentapp/static')
    image = models.ImageField(upload_to='bookmanagmentapp/static')

    def __str__(self):
        return self.bookname