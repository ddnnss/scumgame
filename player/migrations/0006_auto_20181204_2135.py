# Generated by Django 2.1.4 on 2018-12-04 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0005_auto_20181204_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='discord_id',
            field=models.CharField(max_length=30, unique=True, verbose_name='discord id'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=30, unique=True, verbose_name='nickname'),
        ),
        migrations.AlterField(
            model_name='user',
            name='steam_id',
            field=models.CharField(max_length=30, unique=True, verbose_name='steam id'),
        ),
    ]
