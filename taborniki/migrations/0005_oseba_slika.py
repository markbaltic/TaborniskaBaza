# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-14 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taborniki', '0004_auto_20170601_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='oseba',
            name='slika',
            field=models.CharField(default='tralala', max_length=200),
            preserve_default=False,
        ),
    ]
