# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_auto_20151031_0219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='owners',
        ),
        migrations.AlterField(
            model_name='place',
            name='place_image',
            field=models.ImageField(null=True, upload_to=b'static/img/place_media', blank=True),
        ),
    ]
