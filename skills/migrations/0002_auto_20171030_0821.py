# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='slot',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]