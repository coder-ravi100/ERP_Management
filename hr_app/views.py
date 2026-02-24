from django.shortcuts import render

# Create your views here.
def hr_dashboard(request):
    return render(request, 'hr_app/hr_dashboard.html')