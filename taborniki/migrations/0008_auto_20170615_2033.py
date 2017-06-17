# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taborniki', '0007_druzina'),
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
