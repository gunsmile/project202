# Generated by Django 2.2.4 on 2022-04-22 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_saleorder'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SaleOrder',
        ),
    ]