from django.shortcuts import render


def catalog(request):
    return render(request, 'goods/index.html')

def product(request, id):
    return render(request, 'goods/product.html')
