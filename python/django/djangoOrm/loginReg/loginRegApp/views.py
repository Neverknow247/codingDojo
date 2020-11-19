from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

from .models import users

def index(request):
    return redirect('/login')

def login(request):
    return render(request, 'login.html')

def register(request):
    errors = users.objects.basicValidator(request.POST)
    if len(errors) >0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/login')
    else:
        fname = request.POST['firstName']
        lname = request.POST['lastName']
        email = request.POST['email']
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        users.objects.create(firstName=fname, lastName=lname, email=email, password=pw_hash)
        return redirect('/success')

def success(request):
    return render(request, 'success.html')
