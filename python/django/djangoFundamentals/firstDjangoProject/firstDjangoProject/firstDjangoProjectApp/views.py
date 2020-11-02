from django.shortcuts import render, HttpResponse, redirect
def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new():
    return HttpResponse()