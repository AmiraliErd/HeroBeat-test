# Generated by Django 4.2.7 on 2023-11-20 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tracks', '0019_comment_is_published'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='parents',
            new_name='parent',
        ),
    ]
