# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-03-26 22:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_remove_bill_promocode'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillFood',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Bill')),
                ('food_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Food')),
            ],
        ),
        migrations.CreateModel(
            name='BillTobacco',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('count', models.IntegerField(verbose_name='Количество табака')),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Bill')),
                ('tobacco_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Tobacco')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='foods',
            field=models.ManyToManyField(blank=True, to='stock.BillFood'),
        ),
        migrations.AddField(
            model_name='bill',
            name='tobaccos',
            field=models.ManyToManyField(blank=True, to='stock.BillTobacco'),
        ),
    ]
