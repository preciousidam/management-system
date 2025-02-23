# Generated by Django 3.1.3 on 2021-02-22 16:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CorttsAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, unique=True, verbose_name='Account Number')),
                ('name', models.CharField(max_length=255, verbose_name='Account Name')),
                ('bank', models.CharField(max_length=255, verbose_name='Bank')),
                ('sort_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Sort code')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='Created At')),
                ('last_modified', models.DateTimeField(default=datetime.datetime.now, verbose_name='Last Modified')),
                ('account_officer', models.CharField(blank=True, max_length=255, null=True, verbose_name='Account Officer')),
                ('account_officer_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Officer Number')),
            ],
            options={
                'verbose_name_plural': 'Cortts Accounts',
                'ordering': ['bank', 'number'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OtherAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, unique=True, verbose_name='Account Number')),
                ('name', models.CharField(max_length=255, verbose_name='Account Name')),
                ('bank', models.CharField(max_length=255, verbose_name='Bank')),
                ('sort_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Sort code')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='Created At')),
                ('last_modified', models.DateTimeField(default=datetime.datetime.now, verbose_name='Last Modified')),
            ],
            options={
                'verbose_name_plural': 'Other Accounts',
                'ordering': ['bank', 'number'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(verbose_name='Amount')),
                ('type', models.CharField(choices=[('credit', 'credit'), ('debit', 'debit')], max_length=50, verbose_name='Transaction Type')),
                ('mode', models.CharField(choices=[('Cash', 'Cash'), ('Cheque', 'Cheque'), ('Transfer', 'Transfer')], max_length=50, verbose_name='Payment Method')),
                ('desc', models.CharField(max_length=255, verbose_name='Description')),
                ('ben_name', models.CharField(max_length=255, verbose_name='Name')),
                ('ben_phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number')),
                ('receipt', models.ImageField(blank=True, null=True, upload_to='receipt', verbose_name='Evidence')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='Created At')),
                ('last_modified', models.DateTimeField(default=datetime.datetime.now, verbose_name='Last Modified')),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions', to='account.corttsaccount', verbose_name='Account')),
            ],
        ),
    ]
