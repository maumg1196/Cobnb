# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20151030_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='payout_method',
            field=models.CharField(blank=True, max_length=2225, null=True, choices=[(b'D', b'Tarjeta de Debito'), (b'C', b'Tarjeta de Credito'), (b'E', b'Efectivo'), (b'P', b'PayPal')]),
        ),
        migrations.AlterField(
            model_name='place',
            name='type_of_place',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(b'F', b'Food'), (b'T', b'Technologic'), (b'M', b'Medicin'), (b'S', b'School')]),
        ),
    ]
