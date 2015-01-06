# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='longitude',
            field=models.FloatField(blank=True, null=True, validators=(django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(90))),
            preserve_default=True,
        ),
    ]
