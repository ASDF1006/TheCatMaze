# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20181128_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='hint',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
