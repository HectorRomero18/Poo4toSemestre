# Generated by Django 5.2.1 on 2025-07-04 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_tipogasto_remove_doctor_duracion_cita_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiposangre',
            name='descripcion',
            field=models.TextField(verbose_name='Descripción'),
        ),
    ]
