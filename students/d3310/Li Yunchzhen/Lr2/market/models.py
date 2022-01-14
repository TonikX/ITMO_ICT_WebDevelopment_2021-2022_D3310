from operator import mod
from django.db import models
from django.db.models.base import Model


# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=50)
    phone = models.CharField(max_length=32,null=True,blank=True)
    avatar = models.CharField(max_length=20)
    address = models.CharField(max_length=32,null=True,blank=True)
    password = models.CharField(max_length=32)
    wantlist = models.CharField(max_length=100,null=True,blank=True)

class Item(models.Model):
    name = models.CharField(max_length=30)
    pic = models.ImageField(upload_to="market/images")
    description = models.CharField(max_length=200)
    price = models.FloatField()
    wanted = models.IntegerField()
    seller = models.ForeignKey(to=Users, on_delete=models.CASCADE)