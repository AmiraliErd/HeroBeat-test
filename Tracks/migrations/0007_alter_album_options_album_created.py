# Generated by Django 4.2.7 on 2023-11-09 13:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Tracks', '0006_remove_track_artist_track_artist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='album',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
