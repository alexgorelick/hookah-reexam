from django.db import models
from django.contrib.auth.models import AbstractUser
from simple_history.models import HistoricalRecords

import datetime

class Tobacco(models.Model):
    name = models.CharField('Название табака', max_length=30)
    weight = models.IntegerField('Количество табака', default=0)
    cost = models.IntegerField('Стоимость табака', default=0)

    id = models.AutoField(primary_key=True)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.name) + " (" + str(self.weight) + ")"

class Food(models.Model):
    name = models.CharField('Название товара', max_length=30)
    count = models.IntegerField('Количество товара', default=0)
    cost = models.IntegerField('Стоимость товара', default=0)

    id = models.AutoField(primary_key=True)
    history = HistoricalRecords()

    def __str__(self):
        return str(self.name) + " (" + str(self.count) + ")"

class Bill(models.Model):
    id_user = models.IntegerField('ID клиента')
    promocode = models.CharField('Промокод', max_length=10, default="")

    id = models.AutoField(primary_key=True)
    history = HistoricalRecords()

    food = models.ManyToManyField(Food, blank=True)

    def __str__(self):
        return "Заказ №" + str(self.id)	 