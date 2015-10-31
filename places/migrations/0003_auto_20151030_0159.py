# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20151029_0235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='tipo',
        ),
        migrations.AddField(
            model_name='place',
            name='type_of_place',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(b'F', b'Food'), (b'T', b'Technologic'), (b'M', b'Medicin')]),
        ),
        migrations.AlterField(
            model_name='place',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
