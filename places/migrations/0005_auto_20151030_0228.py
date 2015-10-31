# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20151030_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='place_image',
            field=models.ImageField(null=True, upload_to=b'place_media'),
        ),
    ]
