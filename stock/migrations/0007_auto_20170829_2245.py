from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_historicalbill_historicalfood_historicaltobacco'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='cost',
            field=models.IntegerField(default=0, verbose_name='Стоимость товара'),
        ),
        migrations.AddField(
            model_name='historicalfood',
            name='cost',
            field=models.IntegerField(default=0, verbose_name='Стоимость товара'),
        ),
    ]
