# Generated by Django 5.1.3 on 2024-11-27 12:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_alter_news_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
