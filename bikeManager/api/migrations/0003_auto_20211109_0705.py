# Generated by Django 3.2.8 on 2021-11-09 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211105_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='cost',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='bill',
            name='timeFinish',
            field=models.DateTimeField(default=None),
        ),
        migrations.AlterField(
            model_name='bill',
            name='timeStart',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
