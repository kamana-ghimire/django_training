from django.urls import path
from .views import user_profile_home, profile, SignUp

urlpatterns = [
	path("home/", user_profile_home, name="home"),
	path("profile/", profile, name="profile"),
	path("csignup/", SignUp.as_view(), name="csignup"),

]
