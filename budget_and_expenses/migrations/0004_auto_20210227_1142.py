# Generated by Django 3.1.3 on 2021-02-27 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_staff'),
        ('budget_and_expenses', '0003_auto_20210227_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='recipient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.staff', verbose_name='Recipient'),
        ),
    ]
