from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# When calling '/index', login page (login function) should be shown
def login(request):
    return HttpResponse('Hello World!!')

def new(request):
    return HttpResponse('You are in for a surprise!!')