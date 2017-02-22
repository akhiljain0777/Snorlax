from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def startup(request):
	return HttpResponse("<h2>HEY!</h2>")
