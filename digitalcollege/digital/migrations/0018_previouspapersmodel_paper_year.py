# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-05 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0017_previouspapersmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='previouspapersmodel',
            name='paper_year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
