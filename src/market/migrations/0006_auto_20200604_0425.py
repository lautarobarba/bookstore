# Generated by Django 3.0.6 on 2020-06-04 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_auto_20200604_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='nombre'),
        ),
    ]
