# Generated by Django 4.2.9 on 2024-01-26 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_sneakers_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commandes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('prenom', models.CharField(max_length=250)),
                ('adress', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('shoe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.sneakers')),
            ],
        ),
    ]