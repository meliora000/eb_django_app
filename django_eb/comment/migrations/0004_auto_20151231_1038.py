# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-31 01:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('search', '0002_obejct1'),
        ('users', '0002_auto_20151231_1032'),
        ('comment', '0003_auto_20151231_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taste', models.NullBooleanField(default=False)),
                ('mood', models.NullBooleanField(default=False)),
                ('price', models.NullBooleanField(default=False)),
                ('comment', models.CharField(max_length=120, null=True)),
                ('coffee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Object')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.USER')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together=set([('coffee', 'user')]),
        ),
    ]
