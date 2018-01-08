# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taborniki', '0017_auto_20180107_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='akcija',
            name='udelezenci',
            field=models.ManyToManyField(related_name='akcija_clan', to='taborniki.Oseba'),
        ),
    ]
