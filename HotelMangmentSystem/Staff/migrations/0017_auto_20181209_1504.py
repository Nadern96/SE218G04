# Generated by Django 2.1.3 on 2018-12-09 13:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0016_auto_20181209_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='time',
            field=models.TimeField(default=datetime.datetime(2018, 12, 9, 13, 4, 51, 529432, tzinfo=utc)),
        ),
    ]
