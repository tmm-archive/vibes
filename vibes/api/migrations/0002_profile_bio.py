# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 17:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(max_length=140, null=True),
        ),
    ]
