# Generated by Django 4.2.7 on 2023-11-06 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]