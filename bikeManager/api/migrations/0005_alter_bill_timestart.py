# Generated by Django 3.2.8 on 2021-11-13 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20211109_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='timeStart',
            field=models.DateTimeField(),
        ),
    ]