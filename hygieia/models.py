from django.db import models

# Create your models here.

class Projects(models.Model):
	name = models.CharField(max_length=20)
	requested_date = models.DateTimeField(auto_now_add=True)
	creation_date = models.DateTimeField(auto_now=True)
	cpu = models.IntegerField()
	memory = models.IntegerField()
	fCreated = models.BooleanField(default=False)
	type = models.CharField(max_length=10)
	durationHours = models.IntegerField(default=10)
