# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-25 02:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=10)),
                ('stu_sex', models.BooleanField()),
                ('stu_birth', models.DateField()),
                ('stu_create_time', models.DateTimeField(auto_now_add=True)),
                ('stu_operate_time', models.DateTimeField(auto_now=True)),
                ('stu_chinese', models.DecimalField(decimal_places=1, max_digits=3)),
                ('stu_math', models.DecimalField(decimal_places=1, max_digits=3)),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_addr', models.CharField(max_length=30)),
                ('stu_age', models.IntegerField()),
                ('stu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
            options={
                'db_table': 'student_info',
            },
        ),
    ]
