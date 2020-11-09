from django.shortcuts import render, redirect
from .models import users

def index(request):
    context = {
        "allUsers": users.objects.all()
    }
    return render(request, "index.html", context)

def addUser(request):
    context = {
        
    }
    return redirect('/')
