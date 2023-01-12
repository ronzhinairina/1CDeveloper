from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from dev1C.views import *

urlpatterns = [
    path('', index, name='home'),
    path('demand/', demand, name='demand'),
    path('areas/', areas, name='areas'),
    path('skills/', skills, name='skills'),
    path('vacancies/', vacancies, name='vacancies')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)