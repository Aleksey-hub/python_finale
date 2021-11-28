from django.contrib import admin

from catalog.models import Product, CatalogSection

admin.site.register(Product)
admin.site.register(CatalogSection)
