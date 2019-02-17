
from django.contrib import admin
from .models import profile
class ProfileAdmin(admin.ModelAdmin):
	list_display = ("contact_no","address","nationality","grnder","dob","occupation")

admin.site.register(Profile,rofile)
