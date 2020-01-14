# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-29 22:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0005_bill_food'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalBill',
            fields=[
                ('id_user', models.IntegerField(verbose_name='ID клиента')),
                ('promocode', models.CharField(default='', max_length=10, verbose_name='Промокод')),
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'history_date',
                'verbose_name': 'historical bill',
                'ordering': ('-history_date', '-history_id'),
            },
        ),
        migrations.CreateModel(
            name='HistoricalFood',
            fields=[
                ('name', models.CharField(max_length=30, verbose_name='Название товара')),
                ('count', models.IntegerField(default=0, verbose_name='Количество товара')),
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'history_date',
                'verbose_name': 'historical food',
                'ordering': ('-history_date', '-history_id'),
            },
        ),
        migrations.CreateModel(
            name='HistoricalTobacco',
            fields=[
                ('name', models.CharField(max_length=30, verbose_name='Название табака')),
                ('weight', models.IntegerField(default=0, verbose_name='Количество табака')),
                ('cost', models.IntegerField(default=0, verbose_name='Стоимость табака')),
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'history_date',
                'verbose_name': 'historical tobacco',
                'ordering': ('-history_date', '-history_id'),
            },
        ),
    ]
