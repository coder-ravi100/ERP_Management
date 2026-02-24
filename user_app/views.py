from django.shortcuts import render

# Create your views here.
def role_login(request):
    return render(request, 'user_app/login.html')