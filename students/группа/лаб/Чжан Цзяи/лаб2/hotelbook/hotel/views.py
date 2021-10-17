from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import *
from django.views.generic import ListView
from .form import UserForm, CommentForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.
class HotelView(ListView):
    model = Hotel

    def get(self, request):
        hotel = Hotel.objects.get(pk=1)
        rooms = Room.objects.all()
        paginator = Paginator(rooms, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'hotel.html', {'hotel': hotel, 'page_obj': page_obj})


@login_required
def room_info(request, room_id):
    user = User.objects.get(id=request.user.id)
    try:
        room = Room.objects.get(pk=room_id)
    except Room.DoesNotExist:
        pass

    try:
        comments = Comment.objects.filter(room=room_id).all()
        paginator = Paginator(comments, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    except Comment.DoesNotExist:
        pass

    if request.POST.get('user'):
        user_id = int(request.POST.get('user'))

    form = CommentForm(request.POST)
    if form.is_valid():
        new_form = form.save(commit=False)
        new_form.post = form
        new_form.room_id = room_id
        new_form.user_id = user_id
        new_form.save()

        return HttpResponseRedirect('/hotel/{}/'.format(room_id))

    return render(request, 'room.html',
                  {'room': room, 'form': form, 'page_obj': page_obj})


def register(request):
    registered = False

    if request.method == 'POST':

        create_user_form = UserForm(data=request.POST)

        if create_user_form.is_valid():

            user = create_user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True

        else:

            print(create_user_form.errors)
    else:

        create_user_form = UserForm()

    return render(request, 'register.html', {'create_user_form': create_user_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/hotel/')
        else:
            return HttpResponse("Incorrect username or password")

    else:
        return render(request, 'login.html', {})


def order_room(request, room_id):
    user = User.objects.get(id=request.user.id)
    try:
        room = Room.objects.get(pk=room_id)
    except Room.DoesNotExist:
        pass
    if room.order_user == user:
        message = 'You already order this room'
    elif room.order_user is not None and room.order_user != user:
        message = 'You can not order this room'
    else:
        message = 'You successfully order this room'
        user.user_permissions.add('hotel.add_comment')
        room.order_user = User.objects.get(id=request.user.id)
        room.save()
    return render(request, 'order.html', {'message': message})


def cancel_room(request, room_id):
    user = User.objects.get(id=request.user.id)
    try:
        room = Room.objects.get(pk=room_id)
    except Room.DoesNotExist:
        pass
    if room.order_user != user:
        message = 'You did not order this room'
    elif room.order_user == user:
        message = 'You successfully cancel this room'
        room.order_user = None
        room.save()
    return render(request, 'cancel.html', {'message': message})
