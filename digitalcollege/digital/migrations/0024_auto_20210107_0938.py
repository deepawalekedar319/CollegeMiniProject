# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-07 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0023_remove_yearmodel_years'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facuiltymodel',
            name='f_year',
            field=models.IntegerField(),
        ),
    ]
