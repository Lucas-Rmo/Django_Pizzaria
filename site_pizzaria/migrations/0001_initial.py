# Generated by Django 5.0.4 on 2024-10-24 11:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('ingredientes', models.TextField()),
                ('preco', models.FloatField()),
                ('imagem', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Sabor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cliente', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=255)),
                ('borda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_pizzaria.borda')),
                ('pizza1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizza_sabor1', to='site_pizzaria.pizza')),
                ('pizza2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pizza_sabor2', to='site_pizzaria.pizza')),
            ],
        ),
        migrations.AddField(
            model_name='pizza',
            name='sabor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizza_sabor1', to='site_pizzaria.sabor'),
        ),
    ]