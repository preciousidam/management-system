# Generated by Django 3.1.3 on 2021-02-27 15:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0002_auto_20210226_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenancy',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start'),
        ),
    ]
