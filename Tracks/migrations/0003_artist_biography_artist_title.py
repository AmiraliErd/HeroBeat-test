# Generated by Django 4.2.7 on 2023-11-07 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracks', '0002_album_slug_artist_slug_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='biography',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]