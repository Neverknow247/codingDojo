from django.shortcuts import render
from .models import Movie

def index(request):
    context = {
        "allMovies" : Movie.objects.all()
    }
    return render(request, "index.html", context)