from unicodedata import name
from django.urls import path, reverse_lazy
from .views import CorseProfile, CreateCourse, UpdateCourse, DeleteCourse, TklifProfile, CreateTklif, UpdateTklif, DeleteTklif, TklifAnswerAdmin, RegistrationForm
from django.contrib.auth import views as auth_views
app_name = "account"

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("Registration/", RegistrationForm, name="registration"),
    # change password urls
    path('password_change/',auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done')),name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # reset password urls
    path('password_reset/', auth_views.PasswordResetView.as_view(success_url=reverse_lazy('account:password_reset_done')), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url=reverse_lazy('account:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


    path("profile/", CorseProfile.as_view(), name="Profile"),
    path("create-course/", CreateCourse.as_view(), name="CreateCourses"),
    path("update-course/<int:pk>", UpdateCourse.as_view(), name="UpdateCourses"),
    path("delete-course/<int:pk>", DeleteCourse.as_view(), name="DeleteCourses"),
    path("create-homework-list/", TklifProfile.as_view(), name="homework"),
    path("create-tklif/", CreateTklif.as_view(), name="create-tklif"),
    path("update-tklif/<int:pk>", UpdateTklif.as_view(), name="update-tklif"),    
    path("Delete-tklif/<int:pk>", DeleteTklif.as_view(), name="Delete-tklif"),    
    path("tklif-answer-admin/", TklifAnswerAdmin.as_view(), name="tklif-answer-admin"),    


]
