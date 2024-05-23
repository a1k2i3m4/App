from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Category

def index(request):
    context: dict[str,str]={
        'title' : 'Home - Главная',
        'content' : 'Магазин мебели HOME',
    }

    return render(request,'main/index.html',context)
def about(request):
    context: dict[str, str] = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page':"sdfs adsdssad adasasdasdad dsadad"
    }

    return render(request, 'main/about.html', context)
