from django.db import models


class Hero(models.Model):
	name = models.CharField(max_length=60)

	def __str__(self):
		return self.name

class Content(models.Model):
	content = models.CharField(max_length=60, blank =True)

