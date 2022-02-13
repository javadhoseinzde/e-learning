from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import Course, StudentProfile, tklif
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic import View
from django.views.generic.detail import DetailView
from account.mixins import SuperUserAccessProfileMixin


class CourseList(ListView):
    queryset = Course.objects.publish()
    template_name = "learning/home.html"
    context_object_name = "Course"

class CourseDetail(DetailView):
    template_name = "learning/detail.html"

    def get_queryset(self):
        global detail
        slug = self.kwargs.get("slug")
        detail = get_object_or_404(Course, slug=slug)
        return Course.objects.all()

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["detail"] = detail
        return context
    
class ProfessorListCourse(ListView):
    template_name = "learning/Author.html"

    def get_queryset(self):
        global user
        username = self.kwargs.get("username")
        user = get_object_or_404(User, username=username)
        return user.Courses.publish()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = user
        return context

class StudentProfileList(SuperUserAccessProfileMixin , ListView):
    template_name = "learning/Profile.html"
    context_object_name = "proflist"

    def get_queryset(self):
        user = self.kwargs.get("user")
        qry = get_object_or_404(StudentProfile, user=self.request.user)
        return StudentProfile.objects.filter(user=self.request.user)



class TklifList(ListView):
    template_name = "learning/TklifList.html"
    context_object_name = "tklifs"

    def get_queryset(self):
        courses = self.kwargs.get("courses")
        tkl = tklif.objects.filter(courses__students=self.request.user)
        return tklif.objects.filter(courses__students=self.request.user)

