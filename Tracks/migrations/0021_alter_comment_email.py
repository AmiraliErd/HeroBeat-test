# Generated by Django 4.2.7 on 2023-11-20 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracks', '0020_rename_parents_comment_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
