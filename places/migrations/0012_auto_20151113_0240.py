# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_place_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='suite',
        ),
        migrations.AlterField(
            model_name='place',
            name='owner',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
