# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 21:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginreg', '0002_auto_20161115_1100'),
        ('coursesapp', '0002_course_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='users',
        ),
        migrations.AddField(
            model_name='course',
            name='userskey',
            field=models.ManyToManyField(related_name='courseskey', to='loginreg.User'),
        ),
    ]
