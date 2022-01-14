from itertools import chain
from django.core import paginator
from django.core.paginator import EmptyPage, PageNotAnInteger
from django.db.models.fields import PositiveIntegerField
from django.shortcuts import render
from django.http import HttpResponseRedirect, request, response, JsonResponse
import market.models
from django.views.decorators.csrf import csrf_exempt 
from market.models import *
from django.core.paginator import Paginator
# Create your views here.
import os
from piMarket.settings import STATIC_URL


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        avatar = request.POST.get("avatar_seed")
        if username and password:
            dbdata  = Users.objects.filter(username=username).first()
            if dbdata:
                return render(request, 'market/register.html')
            user = Users()
            user.username = username
            user.password = password
            user.avatar = avatar
            user.save()
            return HttpResponseRedirect("/market/login")
    return render(request, 'market/register.html')


def login(request):
    response = render(request, "market/login.html")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            user = Users.objects.filter(username=username).first()
            if user:
                cookies = request.COOKIES.get("login_form")
                if password == user.password:
                    response = HttpResponseRedirect("/market/index")
                    response.set_cookie("username",user.username)
                    request.session["username"] = user.username
                    return response
    return response


def isLogin(func):
    def inner(request, *args, **kwargs):
        cookie_user = request.COOKIES.get("username")
        session_user = request.session.get("username")
        if cookie_user == session_user and cookie_user and session_user:
            user = Users.objects.filter(username=cookie_user).first()
            if user:
                return func(request, **kwargs)
        return HttpResponseRedirect("/market/login")
    return inner


@isLogin
def index(request):
    uname = request.COOKIES.get("username")
    user = Users.objects.filter(username = uname).first()
    avatar = "https://api.multiavatar.com/" + user.avatar + ".svg"
    wlist = str(user.wantlist).split(',')[:-1]
    inwlist =[]
    for item in wlist:
        inwlist.append(int(item))
    itemwanted = Item.objects.filter(pk__in=inwlist)
    all_item = Item.objects.order_by('-pk').all()
    paginator = Paginator(all_item, per_page=6)
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page)
    except PageNotAnInteger:
        current_page = paginator.page(1)
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
    if request.method == "POST":
        user.address = request.POST.get("address")
        user.phone = request.POST.get("phone")
        user.save()
    return render(request, 'market/index.html',{'uname':"Dear "+uname +".", 'uavatar':avatar, 'uphone':user.phone,
                                                'uaddress':user.address,'items': current_page, "item_wanted":itemwanted})

def logout(request):
    response = HttpResponseRedirect("/market/register")
    response.delete_cookie("username")
    del request.session["username"]
    return response


def switchuser(request):
    response = HttpResponseRedirect("/market/login")
    response.delete_cookie("username")
    del request.session["username"]
    return response

def addItem(request):
    response = HttpResponseRedirect("/market/index")
    if request.method == 'POST':
        name = request.POST.get("item_name")
        pic = request.FILES['item_pic']
        uname = request.COOKIES.get("username")
        description = request.POST.get("item_description")
        price = request.POST.get("item_price")
        if name and pic and description and price:
            with open("static/media/"+uname+pic.name, "wb+") as f:
                    for chunk in pic.chunks():
                        f.write(chunk)
            item = Item()
            item.name = name
            item.pic = "/static/media/"+uname+pic.name
            item.description = description
            item.price = price
            item.seller = Users.objects.filter(username=request.session["username"]).first()
            item.wanted = 0
            item.save()

    return response

# @require_GET
# def showItem(request):
#     all_items = Item.objects.order_by('-pk').all()
#     paginator = Paginator(all_items, per_page = 1)
#     page_num = int(request.GET.get("page", 0))
#     if page_num > paginator.num_pages:
#         raise response.Http404
#     item = paginator.page(page_num)
#     if is_ajax(request):
#         #return render(request, 'market/cards.html', {'items':item})
#     #return render(request,'market/card.html',{'items':item})
    

@csrf_exempt
def addwant(request):
    response = HttpResponseRedirect("/market/index")
    if request.is_ajax():
        data = request.POST.get("itemid")
        username = request.session["username"]

        item = Item.objects.filter(id=data).first()

        item.wanted += 1
        item.save()
        user = Users.objects.filter(username=username).first()
        if user.wantlist is None:
            user.wantlist = data+","
            user.save()
        else:
            user.wantlist += data+","
            user.save()
    return response

@csrf_exempt
def removewant(request):
    response = HttpResponseRedirect("/market/index")
    if request.is_ajax():
        data = request.POST.get("itemid")
        username = request.session["username"]
        item = Item.objects.filter(id=data).first()
        item.wanted -= 1
        item.save()
        user = Users.objects.filter(username=username).first()
        wlist = str(user.wantlist).split(',')[:-1]
        wlist.remove(data)
        wlisttmp = ''
        for item in wlist:
            wlisttmp += item+','

        user.wantlist = wlisttmp
        user.save()
    return response

@csrf_exempt
def showliked(request):
    if request.is_ajax() and request.method == "GET":
        username = request.session["username"]
        user = Users.objects.filter(username=username).first()
        wlist = str(user.wantlist)
        wlist = wlist.split(',')
        wlist = wlist[:-1]
    return JsonResponse({"data":wlist})

@csrf_exempt
def checkout(request):
    response = HttpResponseRedirect("/market/index")
    if request.is_ajax() and request.method =="POST":
        itemlist = request.POST.get("itemlist")
        itemlist = itemlist.split(',')
        itemlistin = []
        for item in itemlist:
            itemlistin.append(int(item))
        Item.objects.filter(pk__in=itemlistin).delete()
        Item.save()
    return response