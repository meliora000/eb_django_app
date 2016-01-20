# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-20 04:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20151231_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=datetime.datetime(2016, 1, 20, 4, 2, 29, 80000, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
    ]
