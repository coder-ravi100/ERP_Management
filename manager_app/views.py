from django.shortcuts import render

# Create your views here.
def manager_dashboard(request):
    return render(request, 'manager_app/Dashboard.html')


def my_team(request):
    return render(request, 'manager_app/My_Team.html')