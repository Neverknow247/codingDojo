from django.shortcuts import render
from .models import books, authors

def index(request):
    context = {
        "books" : books.objects.all()
    }
    return render(request, "index.html", context)

def bookView(request, bookNum):
    context = {
        "book" : books.objects.get(id=bookNum)
    }
    return render(request, "book.html", context)

