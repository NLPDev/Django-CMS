# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-27 17:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_addon', '0005_auto_20180926_1129'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FormSavePosition',
            new_name='PluginPosition',
        ),
    ]
