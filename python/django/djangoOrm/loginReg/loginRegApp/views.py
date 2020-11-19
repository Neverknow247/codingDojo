from django.shortcuts import render, redirect
from django.contrib import messages

from .models import users

def index(request):
    return render(request, 'index.html')