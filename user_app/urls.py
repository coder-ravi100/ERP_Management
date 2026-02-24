from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('login_role/', views.role_login, name='role-login')
]