# Generated by Django 4.2.7 on 2023-11-14 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracks', '0012_alter_album_artist_alter_track_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='artist',
            field=models.ManyToManyField(related_name='tracks', to='Tracks.artist'),
        ),
    ]