from django.shortcuts import render
from django.http import HttpResponse

 # Create your views here.

def index2(request):
    return render(request, "index2.html")

def estados(request):
    return render(request, "estadosus.html")

def canada(request):
    return render(request, "canada.html")