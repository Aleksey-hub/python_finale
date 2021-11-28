from django.shortcuts import render

from catalog.models import Product, CatalogSection


def index(request, catalog_section_pk=None):
    catalog_sections = CatalogSection.objects_site.all()

    if catalog_section_pk is None:
        title = 'Главная'
        products = Product.objects_site.prefetch_related('catalog_sections').all()

        context = {
            'title': title,
            'products': products,
            'catalog_sections': catalog_sections,
            'site': request.site,
        }
        return render(request, 'index.html', context)
    else:
        title = 'Каталог'
        products = Product.objects_site.filter(catalog_sections=catalog_section_pk)

        context = {
            'title': title,
            'products': products,
            'catalog_sections': catalog_sections,
            'site': request.site,
        }
        return render(request, 'goods_list.html', context)
