# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-05 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20161205_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bundle',
            name='date_ended',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='bundle',
            name='date_started',
            field=models.DateTimeField(),
        ),
    ]
