# Generated by Django 4.2.9 on 2024-01-09 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sneakers',
            name='brand',
        ),
    ]
