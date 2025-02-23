# Generated by Django 3.1.3 on 2021-02-25 18:15

import budget_and_expenses.models.budgets
import budget_and_expenses.models.expenses
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0002_staff'),
        ('account', '0004_auto_20210225_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(default=budget_and_expenses.models.budgets.ref_number, max_length=50, verbose_name='Ref Number')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(default=budget_and_expenses.models.expenses.ref_number, max_length=50, verbose_name='Ref Number')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('pay_method', models.CharField(choices=[('Cash', 'Cash'), ('Cheque', 'Cheque'), ('Transfer', 'Transfer')], max_length=50, verbose_name='Pay Method')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.expenseaccount', verbose_name='Expense Account')),
                ('recipient', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authentication.staff', verbose_name='Recipient')),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('amount', models.FloatField(verbose_name='Amount')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='budget_and_expenses.category', verbose_name='Category')),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.company', verbose_name='Company')),
                ('expense', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='budget_and_expenses.expense', verbose_name='Expense')),
            ],
        ),
        migrations.CreateModel(
            name='BudgetItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('amount', models.FloatField(verbose_name='Amount')),
                ('budget', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='budget_and_expenses.budget', verbose_name='Budget')),
            ],
        ),
    ]
