from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from articles.forms import LoginForm
import json

# Create your views here.
def login(request):
    form = LoginForm(request, request.POST)
    if form.is_valid():
        auth_login(request,form.get_user())
        context = {
            'form' : form.get_user()
        }
        return render(request,'articles/login.html',context)
    context = {
        'form' : form,
    }
    return render(request,'articles/index.html',context)

def menu(request):
    with open('accounts/static/data.json','r',encoding='utf-8') as f:
        json_data = json.load(f)
    context = {
        'date' : json_data['date'],
        'menu' : json_data['menu']
    }