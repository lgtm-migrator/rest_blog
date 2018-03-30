# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-30 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='device',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_blocked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='timezone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]