# Generated by Django 3.0.6 on 2020-06-20 20:36

from django.db import migrations, models
import market.models.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200616_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=255, unique=True, validators=[market.models.validators.StringWithoutSlashValidator], verbose_name='nombre'),
        ),
    ]
