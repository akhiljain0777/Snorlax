from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponse
#from models import user
from webapp.models import user,restaurant,menu,cart,order
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
	request.session['rname']=request.POST.get('rname')
	r1=restaurant.objects.filter(uname=request.POST.get('rname'))
	m1=menu.objects.filter(uname=request.POST.get('rname'))
	o1=order.objects.create(uname=request.session['uname'],rname=request.session['rname'],status='in_cart')
	request.session['order_id']=o1.id
	request.session['bill_amount']=0
	context = RequestContext(request)
	return render_to_response('webapp/order_page.html',{"menu":m1,"rname":r1[0].name,},context_instance=context)

def addedToCart(request):
	n1=request.POST.get('name')
	p1=request.POST.get('price')
	q1=request.POST.get('quantity')
	m1=menu.objects.filter(uname=request.session['rname'])
	request.session['bill_amount']=request.session['bill_amount']+int(p1)*int(q1)
	c1=cart.objects.filter(order_id=request.session['order_id'],name=n1)
	if len(c1)>0:
		c1[0].quantity=c1[0].quantity+int(q1)
		c1[0].save()
	else:
		c2=cart.objects.create(name=n1,price=p1,quantity=q1,order_id=request.session['order_id'])
	c1=cart.objects.filter(order_id=request.session['order_id'])
	r1=restaurant.objects.filter(uname=request.session['rname'])
	context = RequestContext(request)
	return render_to_response('webapp/cart.html',{"menu":m1,"rname":r1[0].name,"Cart":c1,"total_amount":request.session['bill_amount']},context_instance=context)

def current_cart(request):
	n1=request.POST.get('name')
	p1=request.POST.get('price')
	m1=menu.objects.filter(uname=request.session['rname'])
	r1=restaurant.objects.filter(uname=request.session['rname'])
	c1=cart.objects.filter(order_id=request.session['order_id'],name=n1)
	a=c1[0].quantity
	request.session['bill_amount']=request.session['bill_amount']-int(c1[0].price)*int(a)
	cart.objects.filter(order_id=request.session['order_id'],name=n1).delete()
	c1=cart.objects.filter(order_id=request.session['order_id'])
	context = RequestContext(request)
	if int(request.session['bill_amount'])>0:
		return render_to_response('webapp/cart.html',{"menu":m1,"rname":r1[0].name,"Cart":c1,"total_amount":request.session['bill_amount']},context_instance=context)
	else:
		return render_to_response('webapp/order_page.html',{"menu":m1,"rname":r1[0].name,},context_instance=context)

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
