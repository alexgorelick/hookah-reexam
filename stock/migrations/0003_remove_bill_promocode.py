# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-03-26 20:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20200326_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='promocode',
        ),
    ]