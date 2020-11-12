from django.shortcuts import render, redirect
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
    title = request.POST['title']
    network = request.POST['network']
    releaseDate = request.POST['releaseDate']
    desc = request.POST['desc']
    show = shows.objects.create(title =title, network= network, releaseDate= releaseDate, desc= desc)
    showNum = show.id
    return redirect(f'/shows/{showNum}')

def showView(request, showNum):
    context = {
        "show" : shows.objects.get(id= showNum)
    }
    return render(request, 'showView.html', context)
