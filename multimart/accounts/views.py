from django.shortcuts import render
from .forms import RegisterForm,LoginForm
from django.contrib.auth import authentication,login
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
   form =LoginForm()

   if request.method=="POST":
        form=LoginForm(request.POST)

        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]

            user=authenticate(
                request,
                username=username,
                password=password,
            )
            if user is not None:
                login(request,None)

                if user.role =="seller":
                    return redirect("seller_dashboard")
                elif user.role=="buyer":
                    return redirect("buyer_dashboard")
                
                return redirect("home")
            
            else:
                form.add_error(None,"Invalid username or password")

     return render(request,"account/login.html",{"form":form})






