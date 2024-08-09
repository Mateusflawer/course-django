# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def blog(request):
    return HttpResponse("BLOG 2")

def exemplo(request):
    return HttpResponse("EXEMPLO 2")
