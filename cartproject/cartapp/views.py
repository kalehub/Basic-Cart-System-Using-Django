from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def index(request):
    return render(request, 'cartapp/index.html')



def login_process(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'Hi {username}')
                return redirect('cartapp:index')
            else:
                messages.error(request, 'invalid username or password')
        else:
            messages.error(request, 'failed login attempt')
    form = AuthenticationForm()
    return render(request=request, template_name='cartapp/login.html', context={'login_form':form})

def logout_process(request):
    logout(request)
    messages.info(request, 'Successfully logged out!')
    return redirect('cartapp:login')

def register_process(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST) # fetch data
        print('get form data')
        if form.is_valid(): # check if entered data is valid
            user = form.save()
            print('save form')
            login(request, user) # if success then log in the user
            print('login form')
            messages.success(request, 'Registration successful')
            return redirect('cartapp:index')
        else:
            messages.error(request, 'Registration failed') # if registration failed

    form = NewUserForm()
    return render(request=request, template_name='cartapp/register.html', context={'register_form':form})

def cart(request):
    return HttpResponse('Hello you are at cart')

def checkout(request):
    return HttpResponse('Hello you are at checkout')

