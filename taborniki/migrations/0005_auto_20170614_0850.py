# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taborniki', '0004_auto_20170601_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='druzina',
            name='druzina',
        ),
        migrations.DeleteModel(
            name='Druzina',
        ),
    ]
