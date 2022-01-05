from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Classroom)
admin.site.register(Schedule)
admin.site.register(Student)