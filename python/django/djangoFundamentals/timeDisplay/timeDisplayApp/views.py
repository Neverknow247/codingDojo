from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from time import gmtime, strftime
from datetime import date, datetime
from pytz import timezone
def index(request):
    context = {
        "date": strftime("%b %d,%Y"),
        # "date" : date.today(),
        # "time": datetime.now(timezone('America/Chicago')).strftime("%I:%M %p"),
        "time": strftime("%I:%M %p"),
    }
    return render(request, "index.html", context)


# from datetime import datetime
# from pytz import timezone
# "time": datetime.now(timezone('America/Chicago')).strftime("%I:%M %p")