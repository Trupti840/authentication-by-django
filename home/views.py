from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login

#test user name is trupti and password is Pawar@840

# Create your views here.
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
             # A backend authenticated the credentials
        else:
            return render(request, 'login.html')
            # No backend authenticated the credentials
            #check if user has entered correct credentials
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

