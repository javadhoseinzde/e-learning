from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from learning.models import Course
from .mixins import FieldsMixin, FormValidMixin, UserAccessMixin, SuperUserAccessMixin


class CorseProfile(LoginRequiredMixin, ListView):
	template_name = "account/index.html"
	def get_queryset(self):
		if self.request.user.is_superuser:
			return Course.objects.all()
		else:
			return Course.objects.filter(user=self.request.user) 

class CreateCourse(LoginRequiredMixin,FormValidMixin, FieldsMixin ,CreateView):
	model = Course
	template_name = "account/article-create-update.html"

class UpdateCourse(UserAccessMixin, FormValidMixin, FieldsMixin, UpdateView):
	model = Course
	template_name = "account/article-create-update.html"

class DeleteCourse(SuperUserAccessMixin ,DeleteView):
	model = Course
	success_url = reverse_lazy('account:Profile')
	template_name = "account/delete-course.html"