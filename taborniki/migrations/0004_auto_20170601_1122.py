# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taborniki', '0003_auto_20170601_1121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oseba',
            old_name='mail',
            new_name='email',
        ),
    ]
