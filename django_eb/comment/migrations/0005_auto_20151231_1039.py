# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-31 01:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0004_auto_20151231_1038'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='coffee',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
