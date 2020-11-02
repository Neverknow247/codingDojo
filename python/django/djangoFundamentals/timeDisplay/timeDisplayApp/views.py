from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from time import gmtime, strftime
from datetime import date
today = date.today()
def index(request):
    context = {
        "date": strftime("%b %d,%Y"),
        # "date" : today,
        "time": strftime("%I:%M %p")
    }
    return render(request, "index.html", context)


