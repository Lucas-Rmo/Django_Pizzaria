# Generated by Django 5.0.4 on 2024-10-24 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_pizzaria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='imagem',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
