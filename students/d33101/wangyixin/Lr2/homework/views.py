from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib.auth import authenticate, login
from .models import Student, Studenttopic, Homework
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.http import Http404

# Create your views here.


def index(request):
    pass
    return render(request, 'homework/index.html')


class Login(View):
    def post(self, request):

        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        prompt = "Вход пользователя в систему успешный"

        user = authenticate(username=username, password=password)

        # 判断user是否有效，如果无效则表示认证失败
        if not user:
            prompt = "пароль пользователя неверен！"
        else:
            # 调用login方法来为认证通过的用户创建会话
            login(request, user)
            return redirect('/index')

        return render(request, "homework/login.html", {"prompt": prompt})

    def get(self, request):
        # 如果为get请求，则直接对登录页面进行渲染
        return render(request, "homework/login.html")


class Register(View):
    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password_ = request.POST.get('password_', '')
        email = request.POST.get('email', '')

        prompt = "Успешная регистрация пользователя"
        if not username or not password or password != password_:
            prompt = "Логин или пароль пользователя неверен"
        else:
            # 使用User模型的管理器方法来进行用户对象的创建
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect('/')

        return render(request, "homework/register.html", {"prompt": prompt})

    def get(self, request):
        # 如果为get请求，则直接对注册页面进行渲染
        return render(request, "homework/register.html")


class HomeworkView(ListView):
    model = Homework


class HomeworkCreateView(CreateView):
    model = Studenttopic
    template_name = 'homework_create_view.html'
    fields = ['homework', 'user', 'answer']
    success_url = '/homework'


class StudentCreateView(CreateView):
    model = Student
    template_name = 'student_create_view.html'
    fields = ['name', 'Class', 'email', 'birthday']
    success_url = '/homework'


def work(request, Homework_id):
    try:
        p = Homework.objects.get(pk=Homework_id)
    except Studenttopic.DoesNotExist:
        raise Http404("Homework does not exist")
    return render(request, 'work.html', {'work': p})


class TableView(ListView):
    model = Studenttopic
