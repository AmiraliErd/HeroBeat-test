# Generated by Django 4.2.7 on 2023-11-14 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracks', '0013_alter_track_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='single',
            field=models.BooleanField(default=True),
        ),
    ]
