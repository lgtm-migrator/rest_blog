# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-18 11:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dataset', '0009_auto_20180418_1116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dataset',
            options={'ordering': ['-update']},
        ),
    ]