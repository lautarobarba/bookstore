# Generated by Django 3.0.6 on 2020-06-02 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='nombre')),
                ('last_name', models.CharField(max_length=255, verbose_name='apellido')),
            ],
            options={
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('isbn', models.BigIntegerField(unique=True)),
                ('sinopsis', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('sale', models.CharField(blank=True, choices=[('C', '5%'), ('D', '10%'), ('Q', '15%'), ('V', '20%')], max_length=1, null=True)),
                ('authors', models.ManyToManyField(to='market.Author')),
                ('editorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.Editorial')),
                ('genres', models.ManyToManyField(to='market.Genre')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AddConstraint(
            model_name='book',
            constraint=models.UniqueConstraint(fields=('title', 'editorial'), name='unique title in editorial'),
        ),
    ]
