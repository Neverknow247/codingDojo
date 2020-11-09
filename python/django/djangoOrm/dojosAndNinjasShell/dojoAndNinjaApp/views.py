from django.shortcuts import render, redirect
from .models import dojos, ninjas

def index(request):
    context = {
        "dojoList" : dojos.objects.all()
        # "dojoList" : dojos.objects.get(name = "Best Dojo")
    }
    return render(request, "index.html", context)

def addDojo(request):
    dojos.objects.create(name= request.POST["name"], city= request.POST["city"], state= request.POST["state"])
    return redirect('/')

def addNinja(request):
    fname = request.POST["fname"]
    dojo = request.POST["dojo"]
    do = dojos.objects.get(id=dojo)
    ninjas.objects.create(firstName= fname, lastName= request.POST["lastName"], dojo= do)
    return redirect('/')