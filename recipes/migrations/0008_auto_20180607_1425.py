# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-07 12:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_auto_20180607_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='recipe',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]