from django.shortcuts import render
from .forms import LoginForm
from .models import MenuList
import json

# Create your views here.
def index(request):
    with open('accounts/static/data.json','r',encoding='utf-8') as f:
        json_data = json.load(f)
        if not MenuList.objects.filter(date=json_data['date']):
            for set_menu in json_data['menu']:
                if set_menu['menu_course_type'] == 'L3':
                    for set in set_menu['set_menu_name']:
                        menu = MenuList(
                            date=json_data['date'],
                            menu_course_type='10',
                            set_menu_name=set
                            )
                        menu.save()
                else:
                    menu = MenuList(
                        date=json_data['date'],
                        menu_course_type='20',
                        set_menu_name=' / '.join(set_menu['set_menu_name'])
                        )
                    menu.save()

    form = LoginForm()
    menu_20F = MenuList.objects.filter(date=json_data['date'], menu_course_type='20')
    menu_10F = MenuList.objects.filter(date=json_data['date'], menu_course_type='10')
    context = {
        'form' : form,
        '20F_menu' : menu_20F,
        '10F_menu' : menu_10F
    }
    return render(request, 'articles/index.html', context)

# login은 account에서 처리
# def login(request):
#     form = request.GET
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/login.html', context)