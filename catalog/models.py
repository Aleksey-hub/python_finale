from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64, verbose_name='название')
    add_date = models.DateField(auto_now_add=True, verbose_name='дата поступления')
    price = models.PositiveIntegerField(verbose_name='цена')
    measure_unit = models.CharField(max_length=10, verbose_name='единицы измерения')
    supplier_name = models.CharField(max_length=64, verbose_name='имя поставщика')
    catalog_sections = models.ManyToManyField('CatalogSection', related_name='catalog_sections', verbose_name='раздел каталога')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class CatalogSection(models.Model):
    name = models.CharField(max_length=64, verbose_name='наименование раздела')

    class Meta:
        verbose_name = 'раздел каталога'
        verbose_name_plural = 'разделы каталога'
