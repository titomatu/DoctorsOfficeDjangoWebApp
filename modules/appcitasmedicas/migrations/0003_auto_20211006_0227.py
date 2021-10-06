# Generated by Django 3.2.7 on 2021-10-06 02:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appcitasmedicas', '0002_auto_20211006_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='hora',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appcitasmedicas.citahora'),
        ),
        migrations.AlterField(
            model_name='cita',
            name='hora_cancelada',
            field=models.TimeField(default=datetime.time(2, 27, 16, 357815)),
        ),
        migrations.AlterField(
            model_name='citahora',
            name='hora',
            field=models.TimeField(default=datetime.time(2, 27, 16, 357392)),
        ),
    ]
