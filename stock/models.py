from django.db import models
from django.contrib.auth.models import AbstractUser

import datetime

class Tobacco(models.Model):
    name = models.CharField('Название табака', max_length=30)
    weight = models.IntegerField('Количество табака', default=0)
    cost = models.IntegerField('Стоимость табака', default=0)

    id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.name) + " (" + str(self.weight) + ")"

class Food(models.Model):
    name = models.CharField('Название товара', max_length=30)
    count = models.IntegerField('Количество товара', default=0)
    cost = models.IntegerField('Стоимость товара', default=0)

    id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.name) + " (" + str(self.count) + ")"

class BillTobacco(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey('Bill', on_delete=models.CASCADE)
    tobacco_id = models.ForeignKey('Tobacco', on_delete=models.CASCADE)
    count = models.IntegerField('Количество табака')

    def __str__(self):
        return str(self.tobacco_id.name) + " (" + str(self.count) + ")"

class BillFood(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey('Bill', on_delete=models.CASCADE)
    food_id = models.ForeignKey('Food', on_delete=models.CASCADE)
    count = models.IntegerField('Количество')

    def __str__(self):
        return str(self.food_id.name) + " (" + str(self.count) + ")"

class Bill(models.Model):
    id_user = models.IntegerField('ID клиента')
    id = models.AutoField(primary_key=True)
    sum = models.IntegerField('Итоговая сумма', default=0)
    tobaccos = models.ManyToManyField(BillTobacco, blank=True)
    foods = models.ManyToManyField(BillFood, blank=True)

    def __str__(self):
        return "Заказ №" + str(self.id)