# Generated by Django 3.0.6 on 2020-06-16 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_auto_20200616_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(default='default-cover.png', upload_to='book_cover/', verbose_name='portada'),
        ),
    ]
