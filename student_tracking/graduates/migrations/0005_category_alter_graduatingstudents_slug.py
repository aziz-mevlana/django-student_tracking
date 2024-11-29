# Generated by Django 5.1.3 on 2024-11-27 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graduates', '0004_graduatingstudents_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='graduatingstudents',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
