from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Product

# Create your views here.
@login_required(login_url='cartapp:login')
def index(request):
    # get all object from model
    products = Product.objects.all()
    return render(request, 'cartapp/index.html', context={'products':products})



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
        if form.is_valid(): # check if entered data is valid
            user = form.save()
            login(request, user) # if success then log in the user
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

