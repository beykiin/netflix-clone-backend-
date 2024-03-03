from django.shortcuts import render,redirect
# from django.contrib.auth.models import *
from .form import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import UserProfile as UProfil
# Create your views here.
def userLogin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("browse")
        else:
            return render(request,"login.html")
    
    return render(request,"login.html")

def profiles(request):
    profiller=UProfil.objects.filter(owner=request.user)
    context={
        "profiles":profiller
    }
    return render(request,'browse.html',context)

def register(request):
    form=UserForm()
    if request.method=="POST":
        form=UserForm(request.POST)
        try:
            if form.is_valid:
                form.save()
                return redirect("login")
        except:

            return redirect("register")
    context={
        "form":form
    }
    return render(request,"register.html",context)

def createProfile(request):
    form=UserProfile()
    if request.method=="POST":
        form=UserProfile(request.POST,request.FILES)
        if form.is_valid:
            profil=form.save(commit=False)
            profil.owner=request.user
            profil.save()
            return redirect("browse")

    context={
        "form":form
    }
    return render(request,"create-profile.html",context)

def userAccount(request):
    return render(request,"hesap.html")

def removeAccount(request):
    user=request.user
    user.delete()
    return redirect('index')

def userLogout(request):
    logout(request)
    return redirect("index")