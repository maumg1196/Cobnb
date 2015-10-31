# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_auto_20151031_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='place_image',
            field=models.ImageField(null=True, upload_to=b'static/img/place_media'),
        ),
    ]
