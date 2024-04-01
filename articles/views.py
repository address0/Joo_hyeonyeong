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
                    menu = MenuList(
                    date=json_data['date'],
                    menu_course_type=set_menu['menu_course_type'],
                    set_menu_name=set_menu['set_menu_name']
                    )
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
        '20F_menu' : [menus.get(menu_course_type='L1'),menus.get(menu_course_type='L2')],
        '10F_menu' : menus.get(menu_course_type='L3')
    }
    return render(request, 'articles/index.html', context)

# login은 account에서 처리
# def login(request):
#     form = request.GET
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/login.html', context)