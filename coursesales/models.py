from django.db import models
from django.contrib.auth.models import User

class CourseSales(models.Model):
	title = models.CharField(max_length=100)
	teachers = models.CharField(max_length=100)
	description = models.TextField()
	level = models.CharField(max_length=100)
	price = models.IntegerField(default=0)
	uploadcourse = models.FileField(upload_to="CourseSales/")
	def __str__(self):
		return self.title

class CourseSalesProfile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	courses = models.ManyToManyField(CourseSales)

class PaymentCourseSales(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	courses = models.ManyToManyField(CourseSales)
	is_paid = models.BooleanField(default=False)