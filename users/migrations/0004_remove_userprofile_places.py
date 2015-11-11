# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile_places'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='places',
        ),
    ]
