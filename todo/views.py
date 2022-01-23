from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login

# Create your views here.


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
