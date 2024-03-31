from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User


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
    username= request.POST.get('username')
    first_name= request.POST.get('first_name')
    last_name= request.POST.get('last_name')
    email= request.POST.get('email')
    password1= request.POST.get('password1')
    password2= request.POST.get('password2')
    
    print(username, first_name, last_name, email, password1, password2)
    
    user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
    user.save()
    messages.success(request, 'User created successfully')

    return render(request, 'authapp/register.html')
        
def logout(request):
    auth_logout(request)
    return render(request, 'authapp/login.html')
