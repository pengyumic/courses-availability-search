# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-05 04:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('search_course', '0009_auto_20171204_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
