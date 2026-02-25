from django.shortcuts import render

# Create your views here.
def hr_dashboard(request):
    return render(request, 'hr_app/Dashboard.html')

def employee(request):
    return render(request, 'hr_app/Employee.html')

def employee_add(request):
    return render(request, 'hr_app/Employee_Add.html')

def department(request):
    return render(request, 'hr_app/Department.html')

def department_add(request):
    return render(request, 'hr_app/Department_Add.html')

def designation(request):
    return render(request, 'hr_app/Designation.html')

def designation_add(request):
    return render(request, 'hr_app/Designation_Add.html')

def leave_management(request):
    return render(request, 'hr_app/Leave_management.html')

def apply_leave(request):
    return render(request, 'hr_app/Apply_leave.html')

def Leave_request(request):
    return render(request, 'hr_app/Leave_request.html')

def leave_balance(request):
    return render(request, 'hr_app/Leave_balance.html')