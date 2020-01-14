# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-27 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tobacco',
            fields=[
                ('name', models.CharField(max_length=30, verbose_name='Название табака')),
                ('weight', models.IntegerField(verbose_name='Количество табака')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
