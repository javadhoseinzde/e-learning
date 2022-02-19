from django.http import Http404
from django.shortcuts import get_object_or_404
from learning.models import Course, StudentProfile, tklif

class FieldsMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = ['user', 'slug','name', 'text' ,'level',  'time',  'term_number',  'start_time',  'Status', ]
        elif request.user.is_staff:
            self.fields = ['slug','name', 'text' ,'level',  'time',  'term_number',  'start_time', ]
        else:
            raise Http404("شما اجازه ورود ندارید")
        return super().dispatch(request, *args, **kwargs)

class FormValidMixin():
    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.user = self.request.user
            self.obj.Status = "d"
        return super().form_valid(form)

class UserAccessMixin():
    def dispatch(self, request,pk ,*args, **kwargs):
        course = get_object_or_404(Course, pk=pk)
        if course.user == request.user and course.Status == "d" or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("شما اجازه ورود ندارید")

class SuperUserAccessMixin():
    def dispatch(self, request,*args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("شما اجازه ورود ندارید")


#baraye dastresi b profile khodeshon toye app learning to view estfade shode
class SuperUserAccessProfileMixin():
    def dispatch(self, request,*args, **kwargs):
        stuprof = get_object_or_404(StudentProfile, user=self.request.user)
        if stuprof.user == request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("شما اجازه ورود ندارید")

class FieldsTklifMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = ['user', 'courses', "title","description", "session_number",]
        elif request.user.is_staff:
            self.fields = ['courses', "title","description", "session_number"]
        else:
            raise Http404("شما اجازه ورود ندارید")
        return super().dispatch(request, *args, **kwargs)

class TeacherAccessMixin():
    def dispatch(self, request,pk ,*args, **kwargs):
        tklifs = get_object_or_404(tklif, pk=pk)
        if tklifs.pk == tklifs.pk:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("شما اجازه ورود ندارید")

class FormValidsMixin():
    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.user = self.request.user
            self.obj.cours = Course
        return super().form_valid(form)

class TklifMixin():
    def dispatch(self, request ,*args, **kwargs):
        course = get_object_or_404(Course)
        tklifs = get_object_or_404(tklif)
        if course.user == self.request.user or  tklifs.user == self.request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("شما اجازه ورود ندارید")