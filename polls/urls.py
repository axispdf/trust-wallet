from django import views
from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('send/', views.send, name='send'),
    path('succsess/', views.succsess, name='succsess'),
    path('history/', views.history, name='history'),
    path('erorr/', views.testform, name='test')
]