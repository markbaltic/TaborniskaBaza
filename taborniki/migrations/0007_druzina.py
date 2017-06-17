# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taborniki', '0006_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Druzina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('imeDruzina', models.CharField(max_length=50)),
                ('druzina', models.ForeignKey(related_name='druzina_clan', to='taborniki.Oseba')),
            ],
        ),
    ]
