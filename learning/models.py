from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

class PublishManager(models.Manager):
	def publish(self):
		return self.filter(Status="p")

class Course(models.Model):
	STATUS = (
		("p", "منتشر شده"),
		('d', "پیش نویس"),
	)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Courses", verbose_name="کاربر")
	slug = models.SlugField(max_length=50, unique=True, null=True, verbose_name="ادرس دوره")
	name = models.CharField(max_length=100,verbose_name="اسم دوره")
	text = models.TextField(verbose_name="توضیحات")
	level = models.CharField(max_length=50, verbose_name="سطح کلاس")
	time = models.DateField(verbose_name="تاریخ شروع")
	term_number = models.IntegerField(verbose_name="شماره ترم")
	start_time = models.CharField(max_length=100, verbose_name="ساعت کلاس")
	Status = models.CharField(max_length=10, choices=STATUS, default="d", verbose_name="وضعیت")
	students = models.ManyToManyField(User, blank=True, related_name="student")
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("account:Profile")
	
	
	objects = PublishManager()

class tklif(models.Model):
	courses = models.ForeignKey(Course, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	session_number = models.IntegerField(default=1, null=True,)
	description = models.TextField()


class StudentProfile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name="corses")

	def __str__(self):
		return self.user.username
