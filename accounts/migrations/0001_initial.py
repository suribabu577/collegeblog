# Generated by Django 3.0.7 on 2020-06-20 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='staff_regitser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phn', models.CharField(max_length=10)),
                ('Branch', models.CharField(max_length=10)),
                ('RN', models.CharField(max_length=10)),
                ('idd', models.CharField(max_length=10)),
                ('psw', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='student_regitser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phn', models.CharField(max_length=10)),
                ('Branch', models.CharField(max_length=10)),
                ('RN', models.CharField(max_length=10)),
                ('idd', models.CharField(max_length=10)),
                ('psw', models.CharField(max_length=10)),
            ],
        ),
    ]