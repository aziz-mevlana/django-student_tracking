# Generated by Django 5.1.3 on 2024-11-28 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graduates', '0009_alter_graduatingstudents_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduatingstudents',
            name='img',
            field=models.ImageField(upload_to='graduates'),
        ),
    ]