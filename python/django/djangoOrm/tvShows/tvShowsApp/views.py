from django.shortcuts import render, redirect
from .models import shows

def index(request):
    return redirect('/shows')

def shows(request):
    return render(request, 'shows.html')
