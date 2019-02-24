from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

from .views import user_profile_home, profile, SignUp


urlpatterns = [
	path("home/", user_profile_home, name="home"),
	path("profile/", profile, name="profile"),
	path("csignup/", SignUp.as_view(), name="csignup"),
	path("login/", LoginView.as_view(template_name="login.html"), name="login"),
	path("logout/", LogoutView.as_view(), name="logout",),



]
