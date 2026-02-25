from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [

    path('dashboard/', views.hr_dashboard, name='hr-dashboard'),
    path('employee/', views.employee, name='employee'),
    path('employee_add/', views.employee_add, name='employee-add'),
    
    
    path('department/', views.department, name='department'),
    path('department_add/', views.department_add, name='department-add'),

    path('designation/', views.designation, name='designation'),
    path('designation_add/', views.designation_add, name='designation-add'),

    path('leave_management/', views.leave_management, name='leave-management'),
    path('apply_leave/', views.apply_leave, name='apply-leave'),
    path('Leave_request/', views.Leave_request, name='leave-request'),
    path('leave_balance/', views.leave_balance, name='leave-balance')
]