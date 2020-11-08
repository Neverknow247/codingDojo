from django.shortcuts import render, redirect
def index(request):
    return render(request,"index.html")
        
def createUser(request):
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    context = {
        "name_on_template" : name_from_form,
        "email_on_template" : email_from_form
    }
    return redirect("/success")

def success(request):
    return render(request,"success.html")