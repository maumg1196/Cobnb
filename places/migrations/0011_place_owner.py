# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_userprofile_places'),
        ('places', '0010_auto_20151110_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='owner',
            field=models.ForeignKey(blank=True, to='users.UserProfile', null=True),
        ),
    ]
