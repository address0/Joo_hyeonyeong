from django.shortcuts import render
from .forms import LoginForm
from .models import MenuList
import json

# Create your views here.
def index(request):
    with open('accounts/static/data.json','r',encoding='utf-8') as f:
        json_data = json.load(f)
        for set_menu in json_data['menu']:
            if MenuList.objects.filter(date=json_data['date'], menu_course_type=set_menu['menu_course_type']):
                continue
            else:
                if set_menu['menu_course_type'] == 'L3':
                    for set in set_menu['set_menu_name']:
                        menu = MenuList(
                            date=json_data['date'],
                            menu_course_type=set_menu['menu_course_type'],
                            set_menu_name=set
                            )
                        menu.save()
                else:
                    menu = MenuList(
                        date=json_data['date'],
                        menu_course_type=set_menu['menu_course_type'],
                        set_menu_name=' / '.join(set_menu['set_menu_name'])
                        )
                    menu.save()
                
    form = LoginForm()
    menus = MenuList.objects.filter(date=json_data['date'])
    context = {
        'form' : form,
        '20F_menu' : [menus.get(pk=1),menus.get(pk=2)],
        '10F_menu' : [menus.get(pk=3), menus.get(pk=4), menus.get(pk=5)]
    }
    return render(request, 'articles/index.html', context)

# login은 account에서 처리
# def login(request):
#     form = request.GET
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/login.html', context)