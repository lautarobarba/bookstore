# Generated by Django 3.0.6 on 2020-06-04 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlist',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]