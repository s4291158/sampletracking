# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-04 23:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('st', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='last_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='sample',
            name='time_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
