from .views import *
from django.urls import path
urlpatterns = [
    path('hotel/', HotelView.as_view()),
    path('hotel/<int:room_id>/', room_info),
    path('login', user_login),
    path('register', register),
    path('hotel/<int:room_id>/order', order_room),
    path('hotel/<int:room_id>/cancel', cancel_room),
]
