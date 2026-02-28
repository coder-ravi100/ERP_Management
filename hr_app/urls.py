from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [

    path('dashboard/', views.hr_dashboard, name='hr-dashboard'),

    path('employee/', views.employee, name='employee'),
    path('employee_add/', views.employee_add, name='employee-add'),
    path('update_employee/', views.update_employee, name='update-employee'),
    
    
    path('department/', views.department, name='department'),
    path('department_add/', views.department_add, name='department-add'),

    path('attendance_list/', views.list_attendance, name='list-attendance'),
    path('attendance_mark/', views.attendance_mark, name='mark-attendance'),

    path('leave/', views.leave, name='leave')
]