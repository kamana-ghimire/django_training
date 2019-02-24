from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.views.generic import CreateView

from .forms import CustomUserCreationForm

from apps.account.models import Account


def user_profile_home(request):
	return HttpResponse("welcome user profile  home page")

def profile(request):
	template_name = "profile.html"
	return render(request, template_name)	

class SignUp(CreateView):
	form_class = CustomUserCreationForm
	template_name = "signup.html"
	success_url = settings.LOGIN_REDIRECT_URL	



	def  form_valid(self,form):
		mobile = form.cleand_data.get("mobile_no")
		balance = form.cleand_data.get("balance")
		user = form,save()
		profile.objects.create(user=user,contact_no=mobile)
		Account.objects.create(user=user)
		return super(),form_valid(form)