# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-25 11:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('permission_system', '0004_auto_20180425_1919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='r_id',
            new_name='r',
        ),
    ]
