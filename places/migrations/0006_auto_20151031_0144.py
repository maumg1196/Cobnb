# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20151030_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='place_image',
            field=models.ImageField(null=True, upload_to=b'static/img/event_media'),
        ),
    ]
