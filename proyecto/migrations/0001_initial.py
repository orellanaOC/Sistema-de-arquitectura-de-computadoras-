# Generated by Django 2.0.13 on 2019-12-12 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basurero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.TextField(verbose_name='Código')),
                ('ubicacion', models.TextField(verbose_name='Ubicación')),
                ('estado', models.TextField(default='Activo', verbose_name='Estado')),
            ],
        ),
    ]
