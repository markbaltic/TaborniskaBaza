# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taborniki', '0008_auto_20170615_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rod',
            name='clani',
        ),
        migrations.RemoveField(
            model_name='vod',
            name='clani',
        ),
        migrations.AddField(
            model_name='oseba',
            name='vod',
            field=models.ForeignKey(null=True, to='taborniki.Vod', related_name='vod_clan'),
        ),
        migrations.AlterField(
            model_name='akcije',
            name='organizator',
            field=models.OneToOneField(null=True, to='taborniki.Oseba'),
        ),
        migrations.RemoveField(
            model_name='akcije',
            name='udelezenci',
        ),
        migrations.AddField(
            model_name='akcije',
            name='udelezenci',
            field=models.ManyToManyField(to='taborniki.Oseba', null=True, related_name='akcija_clan'),
        ),
        migrations.AlterField(
            model_name='clanarine',
            name='clan',
            field=models.ForeignKey(null=True, to='taborniki.Oseba', related_name='clanarina_clan'),
        ),
        migrations.AlterField(
            model_name='rod',
            name='nacelnikRod',
            field=models.OneToOneField(null=True, to='taborniki.Oseba', related_name='+'),
        ),
        migrations.AlterField(
            model_name='rod',
            name='staresinaRod',
            field=models.OneToOneField(null=True, to='taborniki.Oseba', related_name='+'),
        ),
        migrations.AlterField(
            model_name='vod',
            name='rod',
            field=models.OneToOneField(null=True, to='taborniki.Rod', related_name='+'),
        ),
        migrations.AlterField(
            model_name='vod',
            name='vodnik',
            field=models.OneToOneField(null=True, to='taborniki.Oseba', related_name='+'),
        ),
    ]
