from django.shortcuts import render
from .models import books, authors

def index(request):
    return render(request, "index.html")
