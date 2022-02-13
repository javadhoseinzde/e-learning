from django.contrib import admin
from .models import Course, StudentProfile, tklif

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