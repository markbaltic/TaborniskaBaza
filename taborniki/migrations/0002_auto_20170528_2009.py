# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taborniki', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Akcije',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imeAkcija', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Clanarine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Druzina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imeDruzina', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Oseba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=50)),
                ('priimek', models.CharField(max_length=50)),
                ('naslov', models.CharField(max_length=100)),
                ('rojstvo', models.DateField()),
                ('telefon', models.IntegerField()),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Rod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imeRod', models.CharField(max_length=50)),
                ('sedez', models.CharField(max_length=50)),
                ('clani', models.ForeignKey(related_name='rod_clan', to='taborniki.Oseba')),
                ('nacelnikRod', models.OneToOneField(related_name='+', to='taborniki.Oseba')),
                ('staresinaRod', models.OneToOneField(related_name='+', to='taborniki.Oseba')),
            ],
        ),
        migrations.CreateModel(
            name='Vod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imeVod', models.CharField(max_length=50)),
                ('clani', models.ForeignKey(related_name='vod_clan', to='taborniki.Oseba')),
                ('rod', models.OneToOneField(related_name='+', to='taborniki.Oseba')),
                ('vodnik', models.OneToOneField(related_name='+', to='taborniki.Oseba')),
            ],
        ),
        migrations.AddField(
            model_name='druzina',
            name='druzina',
            field=models.ForeignKey(related_name='druzina_clan', to='taborniki.Oseba'),
        ),
        migrations.AddField(
            model_name='clanarine',
            name='clan',
            field=models.ForeignKey(related_name='clanarina_clan', to='taborniki.Oseba'),
        ),
        migrations.AddField(
            model_name='akcije',
            name='organizator',
            field=models.OneToOneField(to='taborniki.Oseba'),
        ),
        migrations.AddField(
            model_name='akcije',
            name='udelezenci',
            field=models.ForeignKey(related_name='akcija_clan', to='taborniki.Oseba'),
        ),
    ]
