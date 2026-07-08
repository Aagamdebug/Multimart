from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.

def register(request):
    if request.method=="POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form=RegisterForm()

    return render(request,"accounts/register.html",{"form":form})

def login(request):
    if request.method=="POST":
        form=loginform(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form=loginform()
    
    return render(request,"accounts/login.html")


