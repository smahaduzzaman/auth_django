from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.
@login_required
def index(request):
    return render(request, 'authapp/index.html')
@login_required
def about(request):
    return render(request, 'authapp/about.html')

def login(request):
    username= request.POST.get('username')
    password= request.POST.get('password')
    print(username, password)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        messages.success(request, 'You are successfully logged in') 
        return render(request, 'authapp/index.html')
    else:
        messages.error(request, 'Invalid credentials')
        return render(request, 'authapp/login.html')
    

def register(request):
    
    return render(request, 'authapp/register.html')
