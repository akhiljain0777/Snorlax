from django.shortcuts import render
from django.http import HttpResponse

def login(request):
	return render(request,'webapp/home.html')

def register(request):
	return render(request,'webapp/register.html')

def regSuccess(request):
	
	return render(request,'webapp/regSuccess.html')

