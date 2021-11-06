from django.urls import path
from .views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = "warriors_app"
schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v2',
      description="Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="hardbeat34@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('warriors/', WarriorAPIView.as_view()),
   path('profession/create/', ProfessionCreateAPIView.as_view()),
   path('skill/create/', SkillCreateAPIView.as_view()),
   path('skill/', SkillAPIView.as_view()),
   path('warriors/<int:pk>/', WarriorAllView.as_view()),
   path('warriors/change/<int:pk>/', WarriorSingleView.as_view()),
   path('warriors/list/', WarriorListAPIView.as_view()),
   path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('doc/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]