# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taborniki', '0002_auto_20170528_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oseba',
            name='telefon',
            field=models.CharField(max_length=50),
        ),
    ]
