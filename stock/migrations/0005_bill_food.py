# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-29 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_bill'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='food',
            field=models.ManyToManyField(blank=True, to='stock.Food'),
        ),
    ]
