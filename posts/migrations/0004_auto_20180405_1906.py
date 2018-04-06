# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-05 19:06
from __future__ import unicode_literals

from django.db import migrations, models
import storage.image_storage


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20180405_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, storage=storage.image_storage.ImageStorage(), upload_to=b''),
        ),
    ]
