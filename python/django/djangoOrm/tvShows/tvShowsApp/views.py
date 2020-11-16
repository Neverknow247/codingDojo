from django.shortcuts import render, redirect
from django.contrib import messages
from .models import shows

def index(request):
    return redirect('/shows')

def tvShows(request):
    context = {
        "shows" : shows.objects.all()
    }
    return render(request, 'shows.html', context)

def showNew(request):
    return render(request, 'addShow.html')

def addShow(request):
    errors = shows.objects.basicValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        title = request.POST['title']
        network = request.POST['network']
        releaseDate = request.POST['releaseDate']
        desc = request.POST['desc']
        show = shows.objects.create(title =title, network= network, releaseDate= releaseDate, desc= desc)
        showNum = show.id
        messages.success(request, "Show successfully added")
        return redirect(f'/shows/{showNum}')

def showView(request, showNum):
    context = {
        "show" : shows.objects.get(id= showNum)
    }
    return render(request, 'showView.html', context)

def showEdit(request, showNum):
    context = {
        "show" : shows.objects.get(id= showNum)
    }
    return render(request, 'editShow.html', context)

def editShow(request, showNum):
    errors = shows.objects.basicValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{showNum}/edit')
    else:
        showToEdit = shows.objects.get(id= showNum)
        title = request.POST['title']
        network = request.POST['network']
        releaseDate = request.POST['releaseDate']
        desc = request.POST['desc']
        showToEdit.title = title
        showToEdit.network = network
        showToEdit.releaseDate = releaseDate
        showToEdit.desc = desc
        showToEdit.save()
        return redirect(f'/shows/{showNum}')

def deleteShow(request, showNum):
    showToDelete = shows.objects.get(id = showNum)
    showToDelete.delete()
    return redirect('/')