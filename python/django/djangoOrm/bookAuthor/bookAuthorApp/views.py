from django.shortcuts import render, redirect
from .models import books, authors

def index(request):
    context = {
        "books" : books.objects.all()
    }
    return render(request, "index.html", context)

def bookView(request, bookNum):
    context = {
        "book" : books.objects.get(id=bookNum),
        "authorsList" : authors.objects.all()
    }
    return render(request, "book.html", context)

def bookAdd(request):
    titleForm = request.POST['title']
    descForm = request.POST['desc']
    books.objects.create(title= titleForm, desc= descForm)
    return redirect("/")

def addAuthorToBook(request, bookNum):
    authorForm = request.POST['author']
    author = authors.objects.get(id = authorForm)
    book = books.objects.get(id = bookNum)
    author.books.add(book)
    return redirect(f"/books/{bookNum}")
