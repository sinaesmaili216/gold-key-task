# Generated by Django 4.0.1 on 2022-01-24 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
