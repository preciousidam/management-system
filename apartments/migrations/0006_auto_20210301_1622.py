# Generated by Django 3.1.3 on 2021-03-01 16:22

import apartments.models.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0005_tenancy_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenancy',
            name='end',
            field=models.DateField(default=apartments.models.models.return_date_time, verbose_name='End'),
        ),
        migrations.AlterField(
            model_name='tenancy',
            name='start',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Start'),
        ),
    ]
