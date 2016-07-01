from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

# Create your models here.

class SpoilerVictim(models.Model):

	name = models.CharField(max_length=100, blank=False, null=False)
	tvshow = models.CharField(max_length=100,blank=False, null=False)
	phoneno = models.CharField(max_length=15, validators=[phone_regex], blank=False, null=False)
	status = models.BooleanField(default=True)

	def __unicode__(self):
		if self.name and self.tvshow:
			return self.name + " " + self.tvshow
		else:
			return "Anonymous"	


