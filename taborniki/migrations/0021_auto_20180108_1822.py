# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taborniki', '0020_auto_20180108_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='akcija',
            name='x',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='akcija',
            name='y',
            field=models.FloatField(null=True),
        ),
    ]
