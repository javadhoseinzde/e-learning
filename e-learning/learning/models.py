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
	price = models.IntegerField(default=0)
	Status = models.CharField(max_length=10, choices=STATUS, default="d", verbose_name="وضعیت")
	students = models.ManyToManyField(User, blank=True, related_name="student")
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("account:Profile")
	
	
	objects = PublishManager()

class tklif(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	courses = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="coursess")
	title = models.CharField(max_length=100)
	session_number = models.IntegerField(default=1, null=True,)
	description = models.TextField()
	pic = models.ImageField(upload_to="images/")

	def __str__(self):
		return self.courses.name

class StudentProfile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name="corses")

	def __str__(self):
		return self.user.username

class TklifAnswer(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	taklif = models.ForeignKey(tklif, on_delete=models.CASCADE)
	ansser = models.FileField(upload_to="tklifanser/", verbose_name="جواب سوال")
	
	def __str__(self):
		return self.user.username


class Payment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	cours = models.ManyToManyField(Course, blank=True)
	paid = models.BooleanField(default=False)
	create_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user.username

class Quiz(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	courses = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="courses")
	title = models.CharField(max_length=100)
	pic = models.FileField(upload_to="images/")

	def __str__(self):
		return self.title

class QuizAnswer(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
	ansser = models.FileField(upload_to="tklifanser/", verbose_name="جواب سوال")

	def __str__(self) -> str:
		return self.user.username