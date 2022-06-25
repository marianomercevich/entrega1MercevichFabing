# Generated by Django 4.0.5 on 2022-06-25 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bolso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30, verbose_name='Marca')),
                ('tipo', models.CharField(max_length=30, verbose_name='Tipo')),
                ('talle', models.PositiveSmallIntegerField(choices=[(1, '15 L'), (2, '20 L'), (3, '30 L'), (4, '45 L')], verbose_name='Talle')),
                ('precio', models.FloatField(verbose_name='Precio $')),
            ],
        ),
        migrations.CreateModel(
            name='campera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30, verbose_name='Marca')),
                ('tipo', models.CharField(max_length=30, verbose_name='Tipo')),
                ('talle', models.PositiveSmallIntegerField(choices=[(1, 'XS'), (2, 'S'), (3, 'M'), (4, 'L'), (5, 'XL'), (6, 'XXL')], verbose_name='Talle')),
                ('precio', models.FloatField(verbose_name='Precio $')),
            ],
        ),
        migrations.CreateModel(
            name='casco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30, verbose_name='Marca')),
                ('tipo', models.CharField(max_length=30, verbose_name='Tipo')),
                ('talle', models.PositiveSmallIntegerField(choices=[(1, 'XS 55 CM'), (2, 'S 58 CM'), (3, 'M 60 CM'), (4, 'L 62 CM'), (5, 'XL 63 CM'), (6, 'XXL 65 CM')], verbose_name='Talle')),
                ('precio', models.FloatField(verbose_name='Precio $')),
            ],
        ),
        migrations.CreateModel(
            name='guante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30, verbose_name='Marca')),
                ('tipo', models.PositiveSmallIntegerField(choices=[(1, 'invierno'), (2, 'verano'), (3, '4 estaciones')], verbose_name='Tipo')),
                ('talle', models.PositiveSmallIntegerField(choices=[(1, 'XS'), (2, 'S'), (3, 'M'), (4, 'L'), (5, 'XL'), (6, 'XXL')], verbose_name='Talle')),
                ('precio', models.FloatField(verbose_name='Precio $')),
            ],
        ),
        migrations.CreateModel(
            name='pantalon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30, verbose_name='Marca')),
                ('tipo', models.PositiveSmallIntegerField(choices=[(1, 'invierno'), (2, 'verano'), (3, '4 estaciones')], verbose_name='Tipo')),
                ('talle', models.PositiveSmallIntegerField(choices=[(1, '38'), (2, '40'), (3, '42'), (4, '44'), (5, '46'), (6, '48'), (7, '50'), (8, '52'), (9, '54'), (10, '56')], verbose_name='Talle')),
                ('precio', models.FloatField(verbose_name='Precio $')),
            ],
        ),
    ]
