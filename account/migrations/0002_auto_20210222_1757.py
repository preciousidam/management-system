# Generated by Django 3.1.3 on 2021-02-22 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.FloatField(default=0.0, verbose_name='Amount'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='ben_name',
            field=models.CharField(help_text='Beneficiary name', max_length=255, verbose_name='Beneficiary Name'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='ben_phone_number',
            field=models.CharField(blank=True, help_text='Beneficiary number', max_length=15, null=True, verbose_name='Beneficiary Phone Number'),
        ),
    ]
