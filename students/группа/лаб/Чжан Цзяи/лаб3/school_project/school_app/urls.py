from django.urls import path
from .views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
urlpatterns = [
   path('teachers/list', TeacherListView.as_view()),
   path('teachers/<int:pk>', TeacherRetrieveView.as_view()),
   path('teachers/update/<int:pk>', TeacherUpdateView.as_view()),
   path('teachers/new', TeacherCreateView.as_view()),
   path('teachers/count', TeacherCountView.as_view()),

   path('groups/list', GroupListView.as_view()),
   path('groups/<int:pk>', GroupRetrieveView.as_view()),
   path('groups/update/<int:pk>', GroupUpdateView.as_view()),
   path('groups/new', GroupCreateView.as_view()),

   path('classrooms/list', ClassroomListView.as_view()),
   path('classrooms/<int:pk>', ClassroomRetrieveView.as_view()),
   path('classrooms/update/<int:pk>', ClassroomUpdateView.as_view()),
   path('classrooms/new', ClassroomCreateView.as_view()),
   path('classrooms/count', ClassroomCountBaseView.as_view()),

   path('schedules/list', ScheduleListView.as_view()),
   path('schedules/<int:pk>', ScheduleRetrieveView.as_view()),
   path('schedules/update/<int:pk>', ScheduleUpdateView.as_view()),
   path('schedules/new', ScheduleCreateView.as_view()),

   path('students/list', StudentListView.as_view()),
   path('students/<int:pk>', StudentRetrieveView.as_view()),
   path('students/update/<int:pk>', StudentUpdateView.as_view()),
   path('students/new', StudentCreateView.as_view()),
   path('students/count/<int:pk>', StudentCountGirlView.as_view()),

   path('report/<int:pk>', ReportView.as_view())

]