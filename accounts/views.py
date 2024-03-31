from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate

# Create your views here.
def login(request):
    username = request.POST.get('id')
    password = request.POST.get('password')
    user = authenticate(username=username,password=password)
    if user is not None:
        auth_login(request,user)
        return redirect('articles:login')
    return render(request,'articles/index.html')
