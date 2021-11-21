from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64)
    add_date = models.DateField(auto_now_add=True)
    price = models.PositiveIntegerField()
    measure_unit = models.CharField(max_length=10)
    supplier_name = models.CharField(max_length=64)
