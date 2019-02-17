from django.urls import path
from django.http import HttpResponse

urlpatterns = [
	path("home/",lambda request: HttpResponse("welcome to user home page")),
	]