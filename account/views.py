from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, FormView
from learning.models import Course, tklif, TklifAnswer
from .mixins import (FieldsMixin,
 	FormValidMixin,
  	UserAccessMixin,
   	SuperUserAccessMixin,
    FieldsTklifMixin,
    TeacherAccessMixin,
    FormValidsMixin,
    TklifMixin,
)
from .forms import UserRegistrationForm

class CorseProfile(LoginRequiredMixin, ListView):
	template_name = "account/index.html"
	def get_queryset(self):
		if self.request.user.is_superuser:
			return Course.objects.all().order_by("-pk")
		else:
			return Course.objects.filter(user=self.request.user).order_by("-pk")

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

def RegistrationForm(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
		# Create a new user object but avoid saving it yet
			new_user = user_form.save(commit=False)
			# Set the chosen password
			new_user.set_password(
				user_form.cleaned_data['password'])
			# Save the User object
			new_user.save()
			return redirect("learning:home")

	else:
		user_form = UserRegistrationForm()
		return render(request,
			'registration/RegistrationForm.html',
				{'user_form': user_form})