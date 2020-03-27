from django.contrib import admin
from . import models

admin.site.register(models.Tobacco)
admin.site.register(models.Food)
admin.site.register(models.Bill)
admin.site.register(models.BillTobacco)
admin.site.register(models.BillFood)