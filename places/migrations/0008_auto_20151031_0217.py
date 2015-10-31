# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_auto_20151031_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='place_image',
            field=models.URLField(null=True, blank=True),
        ),
    ]
