# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-04 08:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0005_departmentmodel_d_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departmentmodel',
            name='d_year',
        ),
    ]
