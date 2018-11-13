from django.db import models

# Create your models here.
class Gender(models.Model):
    gender = models.CharField(max_length=80,unique=True)
    def __str__(self):
        return self.gender

class Users(models.Model):
    name = models.CharField(max_length=80,unique=True)
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=80,unique=True)
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
