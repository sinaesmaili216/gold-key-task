# Generated by Django 4.0.1 on 2022-01-24 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0002_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='quantity',
        ),
    ]