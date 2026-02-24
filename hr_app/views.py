from django.shortcuts import render

# Create your views here.
def hr_dashboard(request):
    return render(request, 'hr_app/dashboard.html')

def employee(request):
    return render(request, 'hr_app/Employee.html')

def employee_add(request):
    return render(request, 'hr_app/Employee_Add.html')