from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!.... Hello World!")

def showNbaHome(request):
    return HttpResponse("AHHHHH GOTCHA! NERD!")

def lol(request):
    return HttpResponse("check 12")

def anotherMethod(request,val):
    return HttpResponse(f"You are number {val}")

def google(request):
    return redirect("https://www.google.com/")

def nfl(request):
    return redirect("/nba")

def redir(request):
    return JsonResponse({"response": "JSON response from redirected_method", "status": True})