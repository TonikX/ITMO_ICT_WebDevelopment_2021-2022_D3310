from django.urls import path
from .views import *
from . import views
from .views import *
urlpatterns = [
    path('owner/<int:id_owner>/', views.detail),
    path('time/', example_view),
    path('owner_list/', owner_view),
    path('car/<int:pk>/', CarView.as_view()),
    path('car/list/', CarListView.as_view()),
    path('owner_create', create_owner),
    path('car/<int:pk>/update/', CarUpdateView.as_view()),
    path('car/create/', CarCreateView.as_view()),
    path('car/<int:pk>/delete/', CarDeleteView.as_view()),
]