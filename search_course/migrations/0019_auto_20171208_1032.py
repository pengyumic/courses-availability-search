# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-08 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_course', '0018_auto_20171207_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='sel_crse',
            field=models.CharField(max_length=10, verbose_name='Course Number'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='sel_from_cred',
            field=models.CharField(blank=True, max_length=2, verbose_name='Select from credit'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='sel_title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Course Title'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='sel_to_cred',
            field=models.CharField(blank=True, max_length=2, verbose_name='Select to credit'),
        ),
    ]
