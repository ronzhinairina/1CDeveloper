from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'dev1C/index.html')


def demand(request):
    return render(request, 'dev1C/demand.html')


def areas(request):
    return render(request, 'dev1C/areas.html')


def skills(request):
    return render(request, 'dev1C/skills.html')


def vacancies(request):
    return render(request, 'dev1C/vacancies.html')

# Create your views here.
