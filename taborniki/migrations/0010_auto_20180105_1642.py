# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taborniki', '0009_auto_20180105_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vod',
            name='rod',
            field=models.ForeignKey(related_name='+', to='taborniki.Rod', null=True),
        ),
    ]
