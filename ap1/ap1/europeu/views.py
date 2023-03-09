from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def portugal(request):
    return render(request, "portugal.html")

def espanha(request):
    return render(request, "espanha.html")