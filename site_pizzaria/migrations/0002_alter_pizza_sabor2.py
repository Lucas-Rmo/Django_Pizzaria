# Generated by Django 5.0.4 on 2024-10-23 14:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_pizzaria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='sabor2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pizza_sabor2', to='site_pizzaria.sabor'),
        ),
    ]
