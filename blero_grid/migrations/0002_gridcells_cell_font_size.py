# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-07 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blero_grid', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gridcells',
            name='cell_font_size',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
