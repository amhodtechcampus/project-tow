from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    
    def __str__(self):

        return self.name

class c(models.Model):
    fullname = models.CharField(max_length=400)
    email = models.EmailField()
    
# Create your models here.
