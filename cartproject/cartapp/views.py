from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello you are at index')

def login(request):
    return HttpResponse('Hello you are at login')

def cart(request):
    return HttpResponse('Hello you are at cart')

def checkout(request):
    return HttpResponse('Hello you are at checkout')

