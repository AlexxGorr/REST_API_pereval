# Generated by Django 4.1.6 on 2023-03-06 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0008_perevalimages_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perevalimages',
            old_name='date',
            new_name='data_img',
        ),
    ]
