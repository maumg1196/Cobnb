# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='pirce',
            new_name='price',
        ),
        migrations.AddField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
