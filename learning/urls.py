from django.urls import path
from .views import( 
    CourseList, 
    ProfessorListCourse, 
    CourseDetail, 
    StudentProfileList, 
    TklifList,
    send_request,
    verify,
    UploadAnswer
)
app_name = "learning"

urlpatterns = [
    path("", CourseList.as_view(), name="home"),
    path("detail/<slug:slug>", CourseDetail.as_view(), name="detail"),
    path("professor/<slug:username>/", ProfessorListCourse.as_view(), name="professor"),
    #path("student/profile/", StudentProfileList.as_view(), name="StuProDetail"),
    path("student/profile/", TklifList.as_view(), name="TklifList"),
    path('request/<slug:slug>/', send_request, name='request'),
    path('verify/<slug:slug>/<int:pk>/', verify , name='verify'),
    path('AnswerForm/<int:pk>/', UploadAnswer.as_view() , name='AnswerForm'),

]
