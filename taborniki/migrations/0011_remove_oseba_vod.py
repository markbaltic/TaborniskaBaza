# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taborniki', '0010_auto_20180105_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oseba',
            name='vod',
        ),
    ]
