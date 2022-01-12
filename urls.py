from .views import *
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = "poultry_app"

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
    path('users/list/', UserListAPIView.as_view()),
    path('users/info/<int:pk>', UserInfoAPIView.as_view()),
    path('users/create/', UserCreateAPIView.as_view()),

    path('chickens/list/', ChickenListAPIView.as_view()),
    path('chickens/info/<int:pk>', ChickenInfoAPIView.as_view()),
    path('chickens/create/', ChickenCreateAPIView.as_view()),

    path('breeds/list/', BreedListAPIView.as_view()),
    path('breeds/info/<int:pk>', BreedInfoAPIView.as_view()),
    path('breeds/create/', BreedCreateAPIView.as_view()),

    path('service/list/', ServiceListAPIView.as_view()),
    path('service/info/<int:pk>', ServiceInfoAPIView.as_view()),
    path('service/create/', ServiceCreateAPIView.as_view()),

    path('cells/list/', CellListAPIView.as_view()),
    path('cells/info/<int:pk>', CellInfoAPIView.as_view()),
    path('cells/create/', CellCreateAPIView.as_view()),

    path('service/list/nested/', ServiceNestedAPIView.as_view()),
    path('chickens/list/nested/', ChickenNestedAPIView.as_view()),

    path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
 ]
