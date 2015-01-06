# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.CharField(max_length=15, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=50)),
                ('height', models.IntegerField()),
                ('trunk_diameter', models.IntegerField()),
                ('crown_diameter', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TreeGenre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('species', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tree',
            name='genre',
            field=models.ForeignKey(to='catalog.TreeGenre'),
            preserve_default=True,
        ),
    ]
