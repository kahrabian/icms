# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 21:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20170627_1851'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelOptions(
            name='usercourse',
            options={'verbose_name': 'user course', 'verbose_name_plural': 'user courses'},
        ),
    ]