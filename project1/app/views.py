from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.shortcuts import render


def signin(request):
    if request.method=="POST":
        username = request.POST["username1"]
        password = request.POST["password1"]
        user = auth.authenticate(request,username=username,password=password) #authenticate : 사용자 인증 
        if user is not None:
            auth.login(request,user)
            return render(request, 'index.html')
        else:
            return render(request,'login.html')
    else:
        return render(request, 'login.html') #새 홈페이지 등록

def signup(request):
    if request.method=="POST":
        if request.POST["password01"]== request.POST["password02"]:
            user = User.objects.create_user(
                username = request.POST["username01"],
                password = request.POST["password01"]
            )
            auth.login(request,user) 
            return render(request,'index.html')
        return render(request, 'index.html')
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    return render(request, 'sign.html')
