# Generated by Django 3.0.7 on 2020-06-22 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200622_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='uploaded_at',
            field=models.CharField(max_length=255),
        ),
    ]