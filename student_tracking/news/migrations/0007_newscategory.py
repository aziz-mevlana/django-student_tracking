# Generated by Django 5.1.3 on 2024-11-27 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_delete_graduatingstudents'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
    ]
