from django.contrib import admin
from courses.models import Course, Enrollments
# Register your models here.
admin.site.register(Course)
admin.site.register(Enrollments)