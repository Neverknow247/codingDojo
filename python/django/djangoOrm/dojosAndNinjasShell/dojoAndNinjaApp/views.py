from django.shortcuts import render, redirect
from .models import dojos, ninjas

def index(request):
    context = {
        "dojoList" : dojos.objects.all(),
        "counter" : len(dojos.objects.all())
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

def delete(request):
    dojo = request.POST["dojo"]
    do = dojos.objects.get(id=dojo)
    for i in do.ninja.all():
        ninja = ninjas.objects.get(id=(i.id))
        ninja.delete()
    do.delete()
    return redirect('/')