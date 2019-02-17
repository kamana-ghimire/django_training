from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.

def validate_mobile_no_is_numeric(mobile_no):
	if not mobile_no.isnumeric():
		raise ValidationError(
			_("%(num)s is not valid mobile number"),
			params={"num":mobile_no}
			)

class Profile(models.Model):
	MALE = "m"
	FEMALE = "f"

	GENDER_CHOICE = (
		(MALE, "MALE"),
		(FEMALE, "FEMALE")
		)
	contact_no = models.CharField(max_length=15,
										unique=True,
										verbose_name="mobile no",
										help_text="98xxxxxxxx",
										validators=[validate_mobile_no_is_numeric,])
	address = models.CharField(max_length=50, null=True)
	nationality = models.CharField(max_length=20,  null=True)
	gender = models.CharField(max_length=6,  null=True, choices=GENDER_CHOICE)
	dob = models.DateField( null=True)
	occupation = models.CharField(max_length=20,  null=True)

	def __str__(self):
		return 'contact_no : {} , date of birth :{}'.format(self.contact_no,self.dob )