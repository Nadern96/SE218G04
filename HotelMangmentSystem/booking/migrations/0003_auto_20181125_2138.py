# Generated by Django 2.1.2 on 2018-11-25 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_booking_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_day',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='booking_month',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='booking_year',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='duration',
        ),
        migrations.AddField(
            model_name='booking',
            name='checkin',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='booking',
            name='checkout',
            field=models.DateField(default=None),
        ),
    ]
