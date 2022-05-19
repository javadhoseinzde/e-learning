from django.urls import path
from .views import CourseSalesList, CreateCourseSales, UpdateCourseSales, DeleteCourseSales, CourseSaless, CourseSalessDetail, send_request, verify, CourseSalessLists

app_name = "courseSales"
urlpatterns = [
	path("Course-Sales-List/", CourseSalesList.as_view(), name="CourseSalesList"),	
	path("create-course-sales/", CreateCourseSales.as_view(), name="CreateCourseSales"),	
	path("update-course-sales/<int:pk>/", UpdateCourseSales.as_view(), name="UpdateCourseSales"),
	path("delete-course-sales/<int:pk>/", DeleteCourseSales.as_view(), name="DeleteCourseSales"),
	path("course-sales/", CourseSaless.as_view(), name="CourseSaless"),
	path("course-sales-detail/<slug:slug>/", CourseSalessDetail.as_view(), name="CourseSalessDetail"),

    path('request/<slug:slug>', send_request, name='request'),
    path('verify/<slug:slug>/<int:pk>', verify , name='verify'),
    path('Coursesales-list/', CourseSalessLists.as_view() , name='Coursesalelists'),



]