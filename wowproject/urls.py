"""wowproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#  main urls
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
	path("",lambda request: HttpResponse("welcome  project home page")),
    path('admin/', admin.site.urls),
    path("user/", include("apps.user_profile.urls")),
    path("account/", include("apps.account.urls")),
    path("epocket/", include("apps.epocket.urls")),
    ]
