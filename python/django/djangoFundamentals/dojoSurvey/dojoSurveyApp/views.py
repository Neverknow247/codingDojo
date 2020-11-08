from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def result(request):
    nameFromForm = request.POST['name']
    dojoLocation = request.POST['location']
    favLang = request.POST['language']
    comment = request.POST['comment']
    context = {
        'name' : nameFromForm,
        'location' : dojoLocation,
        'lang' : favLang,
        'comment' : comment
    }
    return render(request, 'route.html', context)
