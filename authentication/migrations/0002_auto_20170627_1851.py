# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-27 18:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0001_initial'),
        ('visage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercourse',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visage.Course', verbose_name='course'),
        ),
        migrations.AddField(
            model_name='usercourse',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.User', verbose_name='user'),
        ),
        migrations.AddField(
            model_name='user',
            name='base_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='base user'),
        ),
        migrations.AddField(
            model_name='user',
            name='courses',
            field=models.ManyToManyField(through='authentication.UserCourse', to='visage.Course', verbose_name='courses'),
        ),
    ]
