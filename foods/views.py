from django.shortcuts import render
from .models import Food, About, Category


# Create your views here.

def home_view(request):
    foods = Food.objects.all().order_by('-id')
    about = About.objects.all().first()
    categories = Category.objects.all()
    context = {
        'foods': foods,
        'about': about,
        'categories': categories
    }
    return render(request, 'index.html', context)


def menu_view(request):
    foods = Food.objects.all().order_by('-id')
    categories = Category.objects.all()
    context = {
        'foods': foods,
        'categories': categories
    }
    return render(request, 'menu.html', context)
