# Generated by Django 3.0.6 on 2020-06-20 20:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0013_auto_20200618_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='value',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)], verbose_name='descuento'),
        ),
    ]
