# Generated by Django 3.0.6 on 2020-06-04 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_auto_20200604_0425'),
        ('shoppingcart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='books',
            field=models.ManyToManyField(to='market.Book'),
        ),
    ]
