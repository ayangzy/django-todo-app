from pickle import NONE
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def home(request):
    return render(request, 'todo/home.html')


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is NONE:
            return render(request, 'todo/loginuser.html', {'form': AuthenticationForm(), 'error': "Username or password does not match"})
        else:
            login(request, user)
            return redirect('currenttodo')
            
            
              
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
    else:
        # create new user here
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], request.POST['password1'])
                user.save()
                login(request, user)
                #return render(request, 'todo/login.html')
                return redirect('currenttodo')
            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': "The username has already been taken, please try another one"})
        else:
            return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': "Password does not match"})

def currenttodo(request):
    return render(request, 'todo/current.html')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
