# Generated by Django 5.1.3 on 2024-11-24 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=False)),
                ('is_home', models.BooleanField(default=False)),
            ],
        ),
    ]
