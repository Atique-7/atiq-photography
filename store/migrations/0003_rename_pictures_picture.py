# Generated by Django 3.2.8 on 2021-10-22 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_pictures_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pictures',
            new_name='Picture',
        ),
    ]
