# Generated by Django 3.2.7 on 2021-10-04 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcitasmedicas', '0009_auto_20210923_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
