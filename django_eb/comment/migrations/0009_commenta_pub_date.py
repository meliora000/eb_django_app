# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-21 00:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0008_auto_20160119_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='commenta',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
