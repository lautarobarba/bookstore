# Generated by Django 3.0.6 on 2020-06-19 16:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0013_auto_20200618_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('c_name', models.CharField(max_length=210, verbose_name='cliente')),
                ('c_email', models.EmailField(max_length=254, verbose_name='email')),
                ('c_pk', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ProductList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Book')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppingcart.Cart')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_title', models.CharField(max_length=255, verbose_name='libro')),
                ('b_editorial', models.CharField(max_length=255, verbose_name='editorial')),
                ('b_price', models.FloatField(verbose_name='precio')),
                ('b_pk', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoppingcart.Order')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='books',
            field=models.ManyToManyField(through='shoppingcart.ProductList', to='market.Book'),
        ),
        migrations.AddField(
            model_name='cart',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
