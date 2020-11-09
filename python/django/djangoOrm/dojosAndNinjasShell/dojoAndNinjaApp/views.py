from django.shortcuts import render, redirect
from .models import dojos, ninjas

def index(request):
    context = {
        "dojoList" : dojos.objects.all()
    }
    return render(request, "index.html", context)

def addDojo(request):
    return redirect('/')

def addNinja(request):
    return redirect('/')