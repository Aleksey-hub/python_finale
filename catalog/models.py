from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.models import Site
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64, verbose_name='название')
    add_date = models.DateField(auto_now_add=True, verbose_name='дата поступления')
    price = models.PositiveIntegerField(verbose_name='цена')
    measure_unit = models.CharField(max_length=10, verbose_name='единицы измерения')
    supplier_name = models.CharField(max_length=64, verbose_name='имя поставщика')
    catalog_sections = models.ManyToManyField('CatalogSection', related_name='catalog_sections', verbose_name='раздел каталога')
    site = models.ManyToManyField(Site)
    objects = models.Manager()
    objects_site = CurrentSiteManager('site')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


class CatalogSection(models.Model):
    name = models.CharField(max_length=64, verbose_name='наименование раздела')
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    objects = models.Manager()
    objects_site = CurrentSiteManager('site')

    class Meta:
        verbose_name = 'раздел каталога'
        verbose_name_plural = 'разделы каталога'
