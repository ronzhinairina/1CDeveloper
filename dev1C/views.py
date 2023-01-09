from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('<h1>main</h1>')


def demand(request):
    return HttpResponse('<h1>demand</h1>')


def areas(request):
    return HttpResponse('<h1>areas</h1>')


def skills(request):
    return HttpResponse('<h1>skills</h1>')


def vacancies(request):
    return HttpResponse('<h1>vacancies</h1>')
# Create your views here.
