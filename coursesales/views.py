from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CourseSales
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from account.mixins import SuperUserAccessMixin


class CourseSalesList(LoginRequiredMixin, SuperUserAccessMixin ,ListView):
	template_name = "coursesales/index.html"
	def get_queryset(self):
		if self.request.user.is_superuser:
			return CourseSales.objects.all()
		else:
			return Http404("اجازه ورود ندارید")

class CreateCourseSales(LoginRequiredMixin, SuperUserAccessMixin ,CreateView):
	fields = ["title", "teachers", "description", "level", "price", "uploadcourse"]
	model = CourseSales
	template_name = "coursesales/article-create-update.html"
	success_url = reverse_lazy("courseSales:CourseSalesList")

class UpdateCourseSales(SuperUserAccessMixin, UpdateView):
	fields = ["title", "teachers", "description", "level", "price", "uploadcourse"]
	model = CourseSales
	template_name = "coursesales/article-create-update.html"
	success_url = reverse_lazy("courseSales:CourseSalesList")


class DeleteCourseSales(SuperUserAccessMixin ,DeleteView):
	model = CourseSales
	success_url = reverse_lazy('courseSales:CourseSalesList')
	template_name = "coursesales/delete-course.html"

class CourseSaless(ListView):
	template_name = "coursesales/courselistview.html"
	model = CourseSales