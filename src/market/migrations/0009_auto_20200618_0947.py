# Generated by Django 3.0.6 on 2020-06-18 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0008_auto_20200616_1404'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['first_name', 'last_name']},
        ),
    ]
