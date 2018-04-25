# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-25 10:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'permission',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=10)),
                ('u_sex', models.BooleanField()),
                ('u_birth', models.DateField()),
                ('u_operate_time', models.DateTimeField(auto_now=True)),
                ('u_create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.AddField(
            model_name='permission',
            name='r',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permission_system.Role'),
        ),
    ]
