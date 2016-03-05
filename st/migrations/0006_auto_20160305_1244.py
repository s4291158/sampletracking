# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-05 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('st', '0005_auto_20160305_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logentry',
            name='geo',
        ),
        migrations.AddField(
            model_name='logentry',
            name='lat',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='logentry',
            name='lng',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
