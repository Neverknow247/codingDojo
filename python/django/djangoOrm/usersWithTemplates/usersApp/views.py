from django.shortcuts import render, redirect
from .models import users

def index(request):
    context = {
        "allUsers": users.objects.all()
    }
    return render(request, "index.html", context)

def addUser(request):
    firstName = request.POST['firstName']
    lastName = request.POST['lastName'] 
    email = request.POST['email'] 
    age = request.POST['age'] 
    context = {
        users.objects.create(firstName= str(firstName), lastName= str(lastName), email= str(email), age= int(age))
    }
    return redirect('/')
