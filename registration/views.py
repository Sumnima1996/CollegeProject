
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


from .forms import *


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if not form.is_valid():
            return render(request, 'registration/register.html',
                          {'form': form})

        else:
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User.objects.create_user(username=username, password=password,
                                     email=email)
            user = authenticate(username=username, password=password)
            login(request, user)
            
            
            return redirect('/')

    else:
        return render(request, 'register.html',
                      {'form': SignUpForm()})




def login(request):

    if request.method == 'POST':
        form =AuthenticationForm(request.POST)
        if not form.is_valid():
            return render(request, 'registration/register.html',
                          {'form': form})

        else:
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            
            
            return redirect('/')

    else:
        return render(request, 'register.html',
                      {'form': AuthenticationForm()})


