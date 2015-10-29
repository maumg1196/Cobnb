# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('suite', models.CharField(max_length=15, null=True, blank=True)),
                ('zip_code', models.CharField(max_length=8)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('place_image', models.ImageField(null=True, upload_to=b'place_media', blank=True)),
                ('pirce', models.IntegerField(default=0)),
                ('payout_method', models.CharField(max_length=2225)),
                ('description', models.TextField(null=True, blank=True)),
                ('meters', models.IntegerField(default=0)),
                ('tipo', models.CharField(max_length=255)),
                ('place_available', models.BooleanField(default=True)),
                ('owners', models.ManyToManyField(to='users.UserProfile')),
            ],
        ),
    ]
