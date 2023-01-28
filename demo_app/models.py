from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_farmer=models.BooleanField(default=False)
    is_agriculturalofficer=models.BooleanField(default=False)
    name = models.CharField(max_length=25,null=True)
    phone = models.CharField(max_length=10,null=True)
    age = models.IntegerField(null=True)
    address = models.TextField(null=True)
    qualification = models.CharField(max_length=15,null=True)
    photo = models.ImageField(upload_to='profile',null=True)
    location = models.CharField(max_length=20,null=True)