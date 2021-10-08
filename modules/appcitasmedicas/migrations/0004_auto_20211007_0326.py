# Generated by Django 3.2.7 on 2021-10-07 03:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('appcitasmedicas', '0003_auto_20211006_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2021, 10, 7, 3, 26, 15, 117242, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cita',
            name='hora_cancelada',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='citahora',
            name='hora',
            field=models.TimeField(default=datetime.datetime(2021, 10, 7, 3, 26, 15, 116859, tzinfo=utc)),
        ),
    ]