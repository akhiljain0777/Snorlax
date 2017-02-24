from django.db import models
from django import forms

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    mobile=models.CharField(max_length=15)
    email=models.CharField(max_length=20)

class restaurant(models.Model):
	name=models.CharField(max_length=30)
	password=models.CharField(max_length=20)
	address=models.CharField(max_length=100)
	mobile=models.CharField(max_length=15)
	email=models.CharField(max_length=20)
	overview=models.CharField(max_length=100)




