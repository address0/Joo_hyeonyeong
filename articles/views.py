from django.shortcuts import render
from .forms import LoginForm

# Create your views here.
def index(request):
    form = LoginForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/index.html', context)

# login은 account에서 처리
# def login(request):
#     form = request.GET
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/login.html', context)