from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [

    path('hr_dashboard/', views.hr_dashboard, name='hr-dashboard'),
]