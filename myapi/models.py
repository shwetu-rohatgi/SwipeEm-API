from __future__ import unicode_literals

from django.db import models

# Create your models here.
class product(models.Model):
	name = models.CharField(max_length=100)
	image = models.FileField(max_length=500, upload_to = 'products')
	price = models.IntegerField()
	shipping_charges = models.IntegerField()
	description = models.TextField()
	brand = models.CharField(max_length=50)
	material = models.CharField(max_length=50)
	gender = models.CharField(max_length=10)
	estimated_arrival =  models.CharField(max_length=10)

	def __unicode__(self):
		return self.name