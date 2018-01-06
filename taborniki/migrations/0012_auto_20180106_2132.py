# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taborniki', '0011_remove_oseba_vod'),
    ]

    operations = [
        migrations.AddField(
            model_name='oseba',
            name='rojstvo2',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='oseba',
            name='vod',
            field=models.ForeignKey(null=True, to='taborniki.Vod', related_name='vod_clan'),
        ),
    ]
