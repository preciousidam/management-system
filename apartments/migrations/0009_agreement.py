# Generated by Django 3.1.3 on 2021-03-05 09:53

import cloudinary_storage.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0008_auto_20210303_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('file', models.FileField(storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='agreement', verbose_name='File')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created AT')),
                ('last_modified', models.DateField(auto_now=True, verbose_name='Last Modified')),
                ('apartment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apartments.apartment', verbose_name='')),
            ],
        ),
    ]
