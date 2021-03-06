# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-27 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='teaching_assistants',
            field=models.ManyToManyField(related_name='ta_course_set', through='visage.CourseTeachingAssistant', to='authentication.User', verbose_name='teaching assistants'),
        ),
    ]
