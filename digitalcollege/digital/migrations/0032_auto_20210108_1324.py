# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-08 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0031_auto_20210108_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='librarymodel',
            name='valid_date',
            field=models.DateTimeField(),
        ),
    ]
