# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-23 16:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20180322_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create',
            field=models.DateField(),
        ),
    ]
