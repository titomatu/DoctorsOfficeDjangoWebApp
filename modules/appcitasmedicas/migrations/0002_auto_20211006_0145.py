# Generated by Django 3.2.7 on 2021-10-06 01:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcitasmedicas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='hora',
            field=models.TimeField(default=datetime.time(1, 45, 40, 361000)),
        ),
        migrations.AlterField(
            model_name='cita',
            name='hora_cancelada',
            field=models.TimeField(default=datetime.time(1, 45, 40, 361040)),
        ),
    ]