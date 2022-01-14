#market url file
from django.conf.urls import handler404
from django.urls import path
from market.views import *

urlpatterns = [
    path('register/', register),
    path('login/',login),
    path('index/', index, name='index'),
    path('logout/',logout),
    path('switchuser/',switchuser),
    path('addItem/',addItem),
    path('addwant',addwant),
    path('removewant',removewant),
    path('showliked',showliked),
    path('checkout',checkout)
]