# Generated by Django 4.2.7 on 2023-11-09 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tracks', '0004_alter_track_artist_alter_track_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='track',
            options={'ordering': ('-created',)},
        ),
    ]
