# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-04 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0008_yearmodel_y_depts'),
    ]

    operations = [
        migrations.AddField(
            model_name='yearmodel',
            name='hod',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]
