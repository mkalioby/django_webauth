# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_webauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='public_key',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
