# Generated by Django 3.2.7 on 2021-10-06 02:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcitasmedicas', '0003_auto_20211006_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='hora_cancelada',
            field=models.TimeField(default=datetime.time(2, 27, 45, 796276)),
        ),
        migrations.AlterField(
            model_name='citahora',
            name='hora',
            field=models.TimeField(default=datetime.time(2, 27, 45, 795772)),
        ),
    ]
