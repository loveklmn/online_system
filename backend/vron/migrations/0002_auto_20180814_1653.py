# Generated by Django 2.1 on 2018-08-14 08:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vron', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progress',
            name='latest_read_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='student',
            name='score',
            field=models.FloatField(default=0),
        ),
    ]
