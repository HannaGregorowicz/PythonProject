# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-26 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20180518_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
