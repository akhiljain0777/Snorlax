from django.db import models
from django import forms

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
