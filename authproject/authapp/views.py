from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'authapp/index.html')

def about(request):
    return render(request, 'authapp/about.html')

def login(request):
    return render(request, 'authapp/login.html')

def register(request):
    return render(request, 'authapp/register.html')