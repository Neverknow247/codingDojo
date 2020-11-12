from django.shortcuts import render, redirect
from .models import books, authors

def index(request):
    context = {
        "books" : books.objects.all()
    }
    return render(request, "index.html", context)

def addAuthor(request):
    context = {
        "authors" : authors.objects.all()
    }
    return render(request, "addAuthor.html", context)

def bookView(request, bookNum):
    context = {
        "book" : books.objects.get(id=bookNum),
        "authorsList" : authors.objects.all()
    }
    return render(request, "book.html", context)

def authorView(request, authorNum):
    context = {
        "author" : authors.objects.get(id=authorNum),
        "bookList" : books.objects.all()
    }
    return render(request, "author.html", context)

def bookAdd(request):
    titleForm = request.POST['title']
    descForm = request.POST['desc']
    books.objects.create(title= titleForm, desc= descForm)
    return redirect("/")

def authorAdd(request):
    firstNameForm = request.POST['firstName']
    lastNameForm = request.POST['lastName']
    noteForm = request.POST['note']
    authors.objects.create(firstName= firstNameForm, lastName= lastNameForm, notes= noteForm)
    return redirect("/addAuthor")

def addAuthorToBook(request, bookNum):
    authorForm = request.POST['author']
    author = authors.objects.get(id = authorForm)
    book = books.objects.get(id = bookNum)
    author.books.add(book)
    return redirect(f"/books/{bookNum}")

def addBookToAuthor(request, authorNum):
    bookForm = request.POST['book']
    book = books.objects.get(id = bookForm)
    author = authors.objects.get(id = authorNum)
    book.author.add(author)
    return redirect(f"/authors/{authorNum}")