# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-05 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0014_ounotesmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ounotesmodel',
            name='oufiles',
            field=models.FileField(default='no pdf', null=True, upload_to='Ou pdfs'),
        ),
    ]