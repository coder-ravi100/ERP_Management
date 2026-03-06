from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login_view(request):

    form = LoginForm()

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            role = user.role.name

            if role == "Super Admin":
                return render(request,"superadmin_dashboard")

            elif role == "HR":
                return render(request,"employee/HR/hr-dashboard")

            elif role == "Manager":
                return render(request,"manager_dashboard")

            elif role == "Employee":
                return render(request,"employee_dashboard")

        else:
            print("Invalid credentials")

    return render(request,"accounts/login.html",{"form":form})
        