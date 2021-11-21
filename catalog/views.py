from django.shortcuts import render

from catalog.models import Product


def index(request):
    title = 'главная'
    products = Product.objects.all()

    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'goods_list.html', context)
