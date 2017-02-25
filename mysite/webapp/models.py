from django.db import models
from django import forms
from django.utils import timezone
#import datetime

# Create your models here.

class user(models.Model):
	uname=models.CharField(max_length=30)
	name = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	address=models.CharField(max_length=100)
	mobile=models.CharField(max_length=15)
	email=models.CharField(max_length=20)

class menu(models.Model):
	name=models.CharField(max_length=50)
	price=models.IntegerField()
	uname=models.CharField(max_length=30)

class restaurant(models.Model):
	uname=models.CharField(max_length=30)
	name=models.CharField(max_length=30)
	password=models.CharField(max_length=20)
	address=models.CharField(max_length=100)
	mobile=models.CharField(max_length=15)
	email=models.CharField(max_length=20)
	overview=models.CharField(max_length=100)
	


class cart(models.Model):
	cart_id=models.IntegerField()
	name=models.CharField(max_length=50)
	price=models.IntegerField()
	quantity=models.IntegerField()


class order(models.Model):
	uname=models.CharField(max_length=30)
	rname=models.CharField(max_length=30)
	order_id=models.IntegerField()
	cart_id=models.IntegerField()	
	payment=models.CharField(max_length=19)
	status=models.CharField(max_length=20)
	order_date = models.DateTimeField("Order Date",auto_now_add=True, blank=True)
	#order_time = models.TimeField(_(u"Order Time"),auto_now_add=True, blank=True)

