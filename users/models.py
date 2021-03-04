from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=200)
    email =  models.CharField(max_length=500)
    phone=  models.CharField(max_length=20, blank=True)