# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-07 01:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('search', '0002_obejct1'),
        ('users', '0002_auto_20151231_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coffee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Object')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.USER')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together=set([('coffee', 'user')]),
        ),
    ]
