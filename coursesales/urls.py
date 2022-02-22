from django.urls import path
from .views import CourseSalesList, CreateCourseSales, UpdateCourseSales, DeleteCourseSales, CourseSaless

app_name = "courseSales"
urlpatterns = [
	path("Course-Sales-List/", CourseSalesList.as_view(), name="CourseSalesList"),	
	path("create-course-sales/", CreateCourseSales.as_view(), name="CreateCourseSales"),	
	path("update-course-sales/<int:pk>/", UpdateCourseSales.as_view(), name="UpdateCourseSales"),
	path("delete-course-sales/<int:pk>/", DeleteCourseSales.as_view(), name="DeleteCourseSales"),
	path("course-sales/", CourseSaless.as_view(), name="CourseSaless")

]