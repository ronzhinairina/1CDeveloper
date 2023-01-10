from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def index(request):
    blocks = Block.objects.filter(page='home')
    context = {'blocks': blocks}
    return render(request, 'dev1C/index.html', context=context)


def demand(request):
    return render(request, 'dev1C/demand.html')


def areas(request):
    return render(request, 'dev1C/areas.html')


def skills(request):
    return render(request, 'dev1C/skills.html')


def vacancies(request):
    return render(request, 'dev1C/vacancies.html')

# Create your views here.
