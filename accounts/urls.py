from django.contrib import admin
from shop.views import home
from django.contrib.auth.views import LoginView
from django.urls import path, include
from accounts.views import login_view



urlpatterns=[
    path('login/',LoginView.as_view(template_name= 'home.html'),name='login'),
    path('main/',login_view,name='main'),
]

