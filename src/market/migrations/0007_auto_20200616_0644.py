# Generated by Django 3.0.6 on 2020-06-16 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_auto_20200604_0425'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name']},
        ),
    ]
