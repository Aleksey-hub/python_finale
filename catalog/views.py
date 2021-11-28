from django.shortcuts import render

from catalog.models import Product, CatalogSection


def index(request):
    title = 'Главная'
    products = Product.objects.prefetch_related('catalog_sections').all()

    catalog_sections = CatalogSection.objects.all()

    context = {
        'title': title,
        'products': products,
        'catalog_sections': catalog_sections,
    }
    return render(request, 'index.html', context)


def catalog_section(request, catalog_section_pk):
    title = 'Каталог'
    products = Product.objects.filter(catalog_sections=catalog_section_pk)

    catalog_sections = CatalogSection.objects.all()

    context = {
        'title': title,
        'products': products,
        'catalog_sections': catalog_sections,
    }
    return render(request, 'goods_list.html', context)
