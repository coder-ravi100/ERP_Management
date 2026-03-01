from django.shortcuts import render

# Create your views here.
def hr_dashboard(request):
    return render(request, 'hr_app/Dashboard.html')

def employee(request):
    return render(request, 'hr_app/All_Employees.html')

def employee_add(request):
    return render(request, 'hr_app/Add_Employee.html')

def update_employee(request):
    return render(request, 'hr_app/Update_Employee.html')

def department_add(request):
    return render(request, 'hr_app/Add_Department.html')

def department(request):
    return render(request, 'hr_app/All_Department.html')

def list_attendance(request):
    return render(request, 'hr_app/Attendance.html')

def attendance_mark(request):
    return render(request, 'hr_app/Attendance_Mark.html')

def leave(request):
    return render(request, 'hr_app/Leave.html')

def payroll(request):
    return render(request, 'hr_app/Payroll.html')

def report(request):  
    return render(request, 'hr_app/Reports.html')

def settings(request):
    return render(request, 'hr_app/Settings.html')

def view_profile(request):
    return render(request, 'hr_app/Show_Profile.html')

def edit_profile(request):
    return render(request, 'hr_app/Edit_Profile.html')