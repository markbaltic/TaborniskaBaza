# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taborniki', '0012_auto_20180106_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oseba',
            name='rojstvo2',
        ),
    ]
