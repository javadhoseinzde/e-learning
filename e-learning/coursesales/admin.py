from django.contrib import admin
from .models import CourseSales, CourseSalesProfile, PaymentCourseSales

admin.site.register(CourseSales)
admin.site.register(CourseSalesProfile)
admin.site.register(PaymentCourseSales)