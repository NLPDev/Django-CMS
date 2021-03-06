# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-28 09:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('dash_docs_app', '0004_remove_documentedmodel_is_documented'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentedmodel',
            name='plugin_id',
        ),
        migrations.AddField(
            model_name='documentedmodel',
            name='parent_plugin',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cms.CMSPlugin'),
            preserve_default=False,
        ),
    ]
