# Generated by Django 3.1.7 on 2021-11-28 16:50

import django.contrib.sites.managers
from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20211128_2006'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='catalogsection',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('objects_site', django.contrib.sites.managers.CurrentSiteManager('site')),
            ],
        ),
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('objects_site', django.contrib.sites.managers.CurrentSiteManager('site')),
            ],
        ),
    ]
