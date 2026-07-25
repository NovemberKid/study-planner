from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def subjects(request):
    return render(request,'subjects.html')

def task(request): 
    return render(request,'task.html')

def contact(request):
    return render(request,'contact.html')

