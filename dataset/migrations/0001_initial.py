# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-12 21:03
from __future__ import unicode_literals

from django.db import migrations, models
import storage.file_storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(storage=storage.file_storage.FileStorage(), upload_to=b'')),
            ],
            options={
                'db_table': 'dataset',
            },
        ),
    ]