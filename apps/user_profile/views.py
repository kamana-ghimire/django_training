from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.views.generic import CreateView

from .forms import CustomUserCreationForm


def user_profile_home(request):
	return HttpResponse("welcome user profile  home page")

def profile(request):
	template_name = "profile.html"
	return render(request, template_name)	

class SignUp(CreateView):
	form_class = CustomUserCreationForm
	template_name = "signup.html"
	success_url = settings.LOGIN_REDIRECT_URL	