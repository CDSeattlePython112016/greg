# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 00:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginreg', '0002_auto_20161115_1100'),
        ('secrets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='secret',
            name='likes',
            field=models.ManyToManyField(related_name='userslike', to='loginreg.User'),
        ),
    ]
