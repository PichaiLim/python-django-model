# Generated by Django 2.1 on 2018-08-10 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180810_1625'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostModal',
            new_name='PostModel',
        ),
    ]