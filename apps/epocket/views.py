from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse("welcome epocket home page")

def contact(request):
	return HttpResponse("this is contact page")

def gallery(request):
	return HttpResponse("this is gallary page")	
def about(request):
	return HttpResponse("this is about page")



