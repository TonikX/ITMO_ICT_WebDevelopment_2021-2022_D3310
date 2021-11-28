"""blogfspo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
urlpatterns = [
    path('admin/', admin.site.urls),
]

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
