from django.shortcuts import render
from goods.models import Category


def index(request):
    return render(request, 'main/index.html', {'categories': Category.objects.all()})


def about(request):
    return render(request, 'main/about.html')
