# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_auto_20151110_0209'),
        ('users', '0002_auto_20151110_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='places',
            field=models.ForeignKey(blank=True, to='places.Place', null=True),
        ),
    ]
