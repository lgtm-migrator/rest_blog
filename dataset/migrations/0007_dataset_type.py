# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-17 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0006_auto_20180417_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='type',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
