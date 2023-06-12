from django.http import HttpResponse
import datetime


from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("Projeto_Final.urls"))
  
]
