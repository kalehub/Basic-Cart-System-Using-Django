from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.

def index(request):
    return HttpResponse('Hello you are at index')

def login_process(request):
    return HttpResponse('Hello you are at login')

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

