# Generated by Django 3.0.7 on 2020-06-22 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200622_1316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upload',
            old_name='img',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='upload',
            old_name='idd',
            new_name='mail',
        ),
    ]