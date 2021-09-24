# Generated by Django 3.1.3 on 2021-09-23 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcitasmedicas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='tipo_id',
            field=models.CharField(choices=[('CC', 'Cédula de Ciudadanía'), ('CE', 'Cédula de Extrangería'), ('PA', 'Pasaporte'), ('PE', 'Permiso de Permanencia'), ('RC', 'Registro Civil'), ('TI', 'Identidad')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='cita',
            name='cancelada',
            field=models.CharField(choices=[('S', 'Si'), ('N', 'No')], max_length=1),
        ),
        migrations.AlterField(
            model_name='medico',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
