from django.db import models

class chkInTime(models.Model):
	name = models.CharField(max_length=200)
	late = models.CharField(max_length=10)
	def __unicode__(self):
		return self.name

	def __unicode__(self):
		return self.late
