# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-11 20:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_friends'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='friends',
            unique_together=set([('user', 'friend')]),
        ),
    ]