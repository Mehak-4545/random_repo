from django.contrib import admin
from django.urls import include, path

# from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('round1/', views.round1, name='round1'),
    path('round2/', views.round2, name='round2'),
    path('round3/', views.round3, name='round3'),
] 