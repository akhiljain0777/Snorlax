from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse
#from models import user
from webapp.models import user,restaurant,menu,order,cart
from django.template import RequestContext
from django.db.models import F,Q

def login(request):
	return render(request,'webapp/home.html')

def loginCheckUser(request):
	q1=user.objects.filter(uname=request.POST.get('uname'),password=request.POST.get('psw'))
	if len(q1)==0:
		return render(request,'webapp/loginFail_user.html')
	request.session['uname']=request.POST.get('uname')
	return redirect('uWelcome')
	#render(request,'webapp/uWelcome.html')

def loginCheckRest(request):
	q1=restaurant.objects.filter(uname=request.POST.get('uname'),password=request.POST.get('psw'))
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
	q1=user.objects.filter(uname=request.POST.get('uname'))
	if len(q1)!=0:
		return render(request,'webapp/register_failed_user.html')
	u1=user.objects.create(uname=request.POST.get('uname'),name=request.POST.get('name'),password=request.POST.get('psw'),address=request.POST.get('add'),mobile=request.POST.get('call'),email=request.POST.get('mail'))
	return render(request,'webapp/regSuccess.html')

def regSuccessRest(request):
	q1=restaurant.objects.filter(uname=request.POST.get('uname'))
	if len(q1)!=0:
		return render(request,'webapp/register_failed_rest.html')
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
	request.session['rname']=request.POST.get('rname')	#check if we need this session
	m1=menu.objects.filter(uname=request.session['rname'])
	context = RequestContext(request)
	return render_to_response('webapp/order_page.html',{"menu":m1,"rname":request.POST.get('rname'),},context_instance=context)

def order_page2(request):
	print 'hi'
	#TODO

'''	request.session['rname']=request.POST.get('rname')	#check if we need this session
	m1=menu.objects.filter(uname=request.session['rname'])
	context = RequestContext(request)

return render_to_response('webapp/order_pa.html',{"menu":m1,"rname":request.POST.get('rname'),},context_instance=context) '''

def checkout(request):
	return redirect('rWelcome')

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


def getCurrentOrders(request):
	#order.objects.create(uname='test',rname='dominos',status='Confirmed')
	print request.session['uname']
	orders=order.objects.filter(rname=request.session['uname'])
	print len(orders)
	#cart.objects.create(cart_id=orders[0].id,name='Palak',price=120,quantity=2)
	context = RequestContext(request)
	return render_to_response('webapp/currentOrders.html',{"orders":orders,},context_instance=context) 

def viewOrder(request):
	request.session['id']= request.POST.get('id')
	orders=order.objects.filter(id=request.POST.get('id'))
	cart_=cart.objects.filter(cart_id=orders[0].id)
	context = RequestContext(request)
	total=0;
	for i in cart_:
		total=total+i.price*i.quantity
	return render_to_response('webapp/viewOrder.html',{"cart_":cart_,"total":total,},context_instance=context) 

def updateStatus(request):
	print request.session['id']
	orders=order.objects.filter(id=request.session['id'])
	orders.status=request.POST.get('OrderStatus')
	print orders.status
	orders[0].save()
	return getCurrentOrders(request)