# Generated by Django 3.0.7 on 2020-06-22 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200621_1100'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='static/')),
                ('text', models.CharField(max_length=255)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='staff_regitser',
            name='Branch',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='staff_regitser',
            name='idd',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='staff_regitser',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='staff_regitser',
            name='psw',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='students_regitser',
            name='idd',
            field=models.CharField(max_length=50),
        ),
    ]