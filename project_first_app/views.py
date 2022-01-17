from django.shortcuts import render
from django.http import Http404
from .models import car_owner, car
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic import ListView
import datetime
from .models import car_owner
from .models import OwnerForm
from django.views.generic.edit import UpdateView, CreateView, DeleteView

# Create your views here.
def detail(request, id_owner):
    try:
        p = car_owner.objects.get(pk=id_owner)
    except car_owner.DoesNotExist:
        raise Http404("owner does not exist")
    return render(request, 'owner.html', {'Owner': p})


def example_view(request):
    # fetch date and time
    now = datetime.datetime.now()
    # convert to string
    html = "Time is {}".format(now)
    # return response
    return HttpResponse(html)


def owner_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization [en]
    # добавление данных об объектах, полученных в результате выполнения запроса exampleModel.objects.all() в словарь
    context["dataset"] = car_owner.objects.all()
    return render(request, "owner_view.html", context)


class CarView(DetailView):
    model = car


class CarListView(ListView):
    model = car
    queryset = model.objects.all()


def create_owner(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = OwnerForm(
        request.POST or None)  # создание экземпляра формы, передача в него данных из формы (из полей в браузере)
    if form.is_valid():  # проверка формы на корректность (валидация)
        form.save()
    context['form'] = form
    return render(request, "create_owner.html", context)


class CarCreateView(CreateView):
    model = car
    fields = ['number_plate', 'car_brand', 'car_model', 'car_color']
    success_url = '/car/list/'


class CarUpdateView(UpdateView):
    model = car
    fields = ['number_plate', 'car_brand', 'car_model', 'car_color']
    success_url = '/car/list/'


class CarDeleteView(DeleteView):
    model = car
    success_url = '/car/list/'