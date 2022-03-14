from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import Course, StudentProfile, tklif, Payment, TklifAnswer
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic import View
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from account.mixins import SuperUserAccessProfileMixin
from django.views.generic.edit import FormView
from .forms import AnswerForms

class CourseList(ListView):
    queryset = Course.objects.publish().order_by("-pk")[0:6]
    template_name = "learning/home.html"
    context_object_name = "Course"

class CourseLists(ListView):
    queryset = Course.objects.publish()
    template_name = "learning/courselists.html"
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


class UploadAnswer(FormView):
    form_class = AnswerForms
    template_name = "learning/AnswerForm.html"
    success_url =reverse_lazy("learning:home")

    def form_valid(self, form, *args, **kwargs):
        pk = self.kwargs.get("pk")
        new_article = TklifAnswer.objects.create(
            user = User.objects.get(pk=self.request.user.id),
            ansser = form.cleaned_data["ansser"],
            taklif = tklif.objects.get(pk=pk),
            )

        form.save(commit = False)
        return super(UploadAnswer, self).form_valid(form)
"""
def UploadAnswer(request, pk):
    
    if request.method == "POST":
        form = AnswerForms(request.POST)

    def form_valid(self, form):
        new_article = TklifAnswer.objects.create(
            user = User.objects.get(pk=self.request.user.id),
            ansser = form.cleaned_data["ansser"],
            taklif = form.cleaned_data["taklif"],
            )

        form.save(commit = False)
        return super(UploadAnswer, self).form_valid(form)

        if form.is_valid():
            new_article = TklifAnswer.objects.create(
                user = User.objects.get(pk=request.user.id),
                title = form.cleaned_data["ansser"],
                message = form.cleaned_data["taklif"],
            )
            new_article.save()
        else:
            return HttpResponse("Error")"""

from django.http import HttpResponse
from django.shortcuts import redirect
from zeep import Client

MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
client = Client('https://sandbox.zarinpal.com/pg/services/WebGate/wsdl')
#amount = 1000  # Toman / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional
 # Important: need to edit for realy server.

def send_request(request,slug):
    p1 = User.objects.get(username = request.user)

    

    course = Course.objects.get(slug=slug)
    amount = int(course.price)
    CallbackURL = f'http://localhost:8000/verify/{course.slug}/{p1.pk}/'
    result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL)
    if result.Status == 100:
        return redirect('https://sandbox.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))

def verify(request,slug, *args, **kwargs):
    course = Course.objects.get(slug=slug)
    amount = int(course.price)
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            pk = kwargs.get("pk")
            p1 = User.objects.get(id=pk)

            courses = Course.objects.get(slug=slug)
            courses.students.add(p1)

            payment = Payment.objects.create(user = p1, paid=True)
            payment.cours.add(courses) 

            return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID)+"  "+ str(p1))
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')