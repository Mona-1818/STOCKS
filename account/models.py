from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True) 


    def __str__(self):
        return self.username
    
class UserProfile(models.Model):
    email = models.EmailField(unique=True) 
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=20, blank=True, null=True)
    Number = models.BigIntegerField(blank=True, null=True)
    Portfolio_amount = models.BigIntegerField(blank=True, null=True)
    # Image = models.ImageField(upload_to='images/', null=True, blank=True)
    Desc = models.CharField(max_length=2000, blank=True, null=True)
    occupation = models.CharField(max_length=2000, blank=True, null=True) 
    def __str__(self):
        return self.username
    
class portfolio(models.Model):
    username = models.CharField(max_length=20, blank=True, null=True)
    companyname=models.CharField(max_length=20, blank=True, null=True)
    quantity = models.IntegerField( blank=True, null=True)
    price = models.FloatField( blank=True, null=True)