# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-04 09:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0009_yearmodel_hod'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacuiltyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('pno', models.CharField(max_length=12)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facuilty_dept', to='digital.DepartmentModel')),
                ('f_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facuilty_year', to='digital.YearModel')),
            ],
        ),
    ]