from django.shortcuts import render
from django.http import HttpResponse

def user_profile_home(request):
	return HttpResponse("welcome user profile  home page")

def profile(request):
	template_name = "profile.html"
	return render(request, template_name)	