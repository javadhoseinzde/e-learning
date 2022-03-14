from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CourseSales, CourseSalesProfile
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from account.mixins import SuperUserAccessMixin
from django.contrib.auth.models import User


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

class CourseSalessDetail(DetailView):
	template_name = "coursesales/coursedetailview.html"

	def get_queryset(self):
		global detail
		slug = self.kwargs.get("slug")
		detail = get_object_or_404(CourseSales,slug=slug)
		return CourseSales.objects.filter(slug=slug)

	def get_context_data(self, **kwargs):
	    context =  super().get_context_data(**kwargs)
	    context["detail"] = detail
	    return context


from django.http import HttpResponse
from django.shortcuts import redirect
from zeep import Client

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
    p2 = User.objects.get(username = request.user)


    coursesale = CourseSales.objects.get(slug=slug)
    amount = int(coursesale.price)
    CallbackURL = f'http://localhost:8000/verify/{coursesale.slug}/{p2.pk}'
    result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL)
    if result.Status == 100:
        return redirect('https://sandbox.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))

def verify(request,slug, *args, **kwargs):
    coursesale = CourseSales.objects.get(slug=slug)
    amount = int(coursesale.price)
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            pk = kwargs.get("pk")
            p2 = User.objects.get(id=pk)
            coursesale = CourseSales.objects.get(slug=slug)
            Coursesalesprofile = CourseSalesProfile.objects.create(
                user = p2,
                )
            Coursesalesprofile.courses.add(coursesale)
            return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')