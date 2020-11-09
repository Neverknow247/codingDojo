from django.shortcuts import render, redirect
from models import dojos, ninjas

def index(request):
    return render(request, "index.html")
