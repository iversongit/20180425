# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-25 06:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20180425_1409'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='class_id',
            new_name='classroom',
        ),
    ]
