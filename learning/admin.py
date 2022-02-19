from django.contrib import admin
from .models import Course, StudentProfile, tklif, Payment, TklifAnswer

class CourseAdmin(admin.ModelAdmin):
	list_display = ("user", "name", "level", "time", "Status")
	list_filter = (["time"])
	search_filed = ("name", "level")
	prepopulated_fields = {'slug':("name",)}

admin.site.register(Course, CourseAdmin)
class StudentProfileAdmin(admin.ModelAdmin):
	list_display = ("user",)

admin.site.register(StudentProfile, StudentProfileAdmin)


class StudentTaklifAdmin(admin.ModelAdmin):
	list_display = ("pk","title","description", "session_number")

admin.site.register(tklif, StudentTaklifAdmin)

class PaymentAdmin(admin.ModelAdmin):
	list_display = ("user","paid","courses","create_time")
	list_filter = (["create_time", "paid"])
	def courses(self, obj):
		return "\n".join([p.name for p in obj.cours.all()])


admin.site.register(Payment, PaymentAdmin)


class AnswerAdmin(admin.ModelAdmin):
	list_display = ("user","taklif","ansser")


admin.site.register(TklifAnswer, AnswerAdmin)