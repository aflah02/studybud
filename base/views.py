from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home page")

def room(request):
    return HttpResponse("Room page")
# Create your views here.
