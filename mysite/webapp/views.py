from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse
#from models import user
from webapp.models import user,restaurant,menu
from django.template import RequestContext
from django.db.models import F,Q

def login(request):
	return render(request,'webapp/home.html')

def loginCheckUser(request):
	q1=user.objects.filter(uname=request.POST.get('uname'),password=request.POST.get('psw'))
	print q1
	if len(q1)==0:
		return render(request,'webapp/loginFail_user.html')
	request.session['uname']=request.POST.get('uname')
	return redirect('uWelcome')
	#render(request,'webapp/uWelcome.html')

def loginCheckRest(request):
	q1=restaurant.objects.filter(uname=request.POST.get('uname'),password=request.POST.get('psw'))
	print q1
	if len(q1)==0:
		return render(request,'webapp/loginFail_rest.html')
	request.session['uname']=request.POST.get('uname')
	return redirect('rWelcome')
	#render(request,'webapp/uWelcome.html')



def uWelcome(request):
	return render(request,'webapp/uWelcome.html')

def rWelcome(request):
	return render(request,'webapp/rWelcome.html')

def registerUser(request):
	return render(request,'webapp/register.html')

def registerRest(request):
	return render(request,'webapp/register_rest.html')


def regSuccessUser(request):
	u1=user.objects.create(uname=request.POST.get('uname'),name=request.POST.get('name'),password=request.POST.get('psw'),address=request.POST.get('add'),mobile=request.POST.get('call'),email=request.POST.get('mail'))
	return render(request,'webapp/regSuccess.html')

def regSuccessRest(request):
	u1=restaurant.objects.create(uname=request.POST.get('uname'),name=request.POST.get('name'),password=request.POST.get('psw'),address=request.POST.get('add'),mobile=request.POST.get('call'),email=request.POST.get('mail'))
	return render(request,'webapp/regSuccess.html')

def search(request):
	print request.session['uname']
	query = request.POST.get('q')
	query=str(query)
	qset = Q()
	for term in query.split():
		qset |= Q(name__contains=term)
	results = restaurant.objects.filter(qset)
	context = RequestContext(request)
	return render_to_response('webapp/results.html', {"results": results,},context_instance=context)

def order_page(request):
	return render(request,'webapp/order_page.html')

def editMenu(request):
	m1=menu.objects.filter(uname=request.session['uname'])
	context = RequestContext(request)
	return render_to_response('webapp/editMenu.html',{"m1":m1,},context_instance=context)

def addMenuItem(request):
	return render(request,'webapp/addMenuItem.html')

def menuItemAdded(request):
	m1=menu.objects.create(name=request.POST.get('name'),price=request.POST.get('price'),uname=request.session['uname'])
	return redirect('editMenu')

def removeMenuItem(request):
	menu.objects.filter(name=request.POST.get('name'),price=request.POST.get('price'),uname=request.session['uname']).delete()
	m1=menu.objects.filter(uname=request.session['uname'])
	context = RequestContext(request)
	return redirect('editMenu')
