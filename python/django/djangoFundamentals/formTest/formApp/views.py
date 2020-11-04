from django.shortcuts import render
def index(request):
    return render(request,"index.html")
        
def create_user(request):
    print("Got Post Info....................")
    print(request.POST)
    return render(request,"index.html")