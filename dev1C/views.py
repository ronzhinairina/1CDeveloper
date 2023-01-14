from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .data_science import get_hh_dev1C


def index(request):
    blocks = Block.objects.filter(page='home')
    context = {'blocks': blocks}
    return render(request, 'dev1C/index.html', context=context)


def demand(request):
    blocks = Block.objects.filter(page='demand')
    context = {'blocks': blocks}
    return render(request, 'dev1C/demand.html', context=context)


def areas(request):
    blocks = Block.objects.filter(page='areas')
    context = {'blocks': blocks}
    return render(request, 'dev1C/areas.html', context=context)


def skills(request):
    blocks = Block.objects.filter(page='skills')
    context = {'blocks': blocks}
    return render(request, 'dev1C/skills.html', context=context)


def vacancies(request):
    vacancies = get_hh_dev1C.get_hh_dev1C()
    context = {'vacancies': vacancies}
    return render(request, 'dev1C/vacancies.html', context=context)

# Create your views here.
