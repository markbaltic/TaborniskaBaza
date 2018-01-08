# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taborniki', '0018_auto_20180108_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akcija',
            name='udelezenci',
            field=models.ManyToManyField(related_name='akcija_clan', null=True, to='taborniki.Oseba'),
        ),
    ]
