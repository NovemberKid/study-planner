from django.shortcuts import render

# Create your views here.
def all_planner(request):
    return render(request, 'planner/all_planner.html')

def dashboard(request):
    return render(request, 'planner/dashboard.html')



