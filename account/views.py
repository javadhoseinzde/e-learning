from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from learning.models import Course, tklif, TklifAnswer
from .mixins import (FieldsMixin,
 	FormValidMixin,
  	UserAccessMixin,
   	SuperUserAccessMixin,
    FieldsTklifMixin,
    TeacherAccessMixin,
    FormValidsMixin,
    TklifMixin
)


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


class TklifProfile(LoginRequiredMixin ,ListView):
	template_name = "account/tklifprofile.html"
	def get_queryset(self):
		if self.request.user.is_superuser:
			return tklif.objects.all()
		else:
			return tklif.objects.filter(user=self.request.user) 


class CreateTklif(LoginRequiredMixin,FieldsTklifMixin,FormValidsMixin,CreateView):
	model = tklif
	template_name = "account/create-update-tklif.html"
	success_url = reverse_lazy("account:Profile")

class UpdateTklif(LoginRequiredMixin,FieldsTklifMixin,FormValidsMixin, UpdateView):
	model = tklif
	template_name = "account/create-update-tklif.html"
	success_url = reverse_lazy("account:Profile")
	

class DeleteTklif(DeleteView):
	model = tklif
	success_url = reverse_lazy('account:Profile')
	template_name = "account/delete-tklif.html"

class TklifAnswerAdmin(LoginRequiredMixin ,ListView):
	template_name = "account/TklifProfileAdmin.html"
	def get_queryset(self):
		if self.request.user.is_superuser:
			return TklifAnswer.objects.all()
		else:
			return TklifAnswer.objects.filter(taklif__user = self.request.user) 
