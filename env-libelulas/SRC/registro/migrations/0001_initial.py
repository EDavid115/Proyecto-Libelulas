# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registrado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=50)),
                ('codigo', models.CharField(max_length=60)),
                ('correo', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
    ]
