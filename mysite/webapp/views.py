from django.shortcuts import render,redirect
from django.http import HttpResponse
#from models import user
from webapp.models import user

def login(request):
	return render(request,'webapp/home.html')

def loginCheck(request):
	q1=user.objects.filter(name=request.POST.get('uname'),password=request.POST.get('psw'))
	print q1
	if len(q1)==0:
		return render(request,'webapp/loginFail.html')
	return redirect('uWelcome')
	#render(request,'webapp/uWelcome.html')

def uWelcome(request):
	return render(request,'webapp/uWelcome.html')

def register(request):
	return render(request,'webapp/register.html')

def regSuccess(request):
	u1=user.objects.create(name=request.POST.get('name'),password=request.POST.get('psw'))
	return render(request,'webapp/regSuccess.html')

