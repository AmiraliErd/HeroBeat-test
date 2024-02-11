# Generated by Django 4.2.7 on 2023-11-09 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracks', '0007_alter_album_options_album_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='artist',
            field=models.ManyToManyField(to='Tracks.artist'),
        ),
        migrations.AlterField(
            model_name='track',
            name='category',
            field=models.ManyToManyField(to='Tracks.category'),
        ),
    ]
